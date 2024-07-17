import keras
import matplotlib.pyplot as pyplot
import numpy

def get_img_array(img_path, target_size):
    img = keras.utils.load_img(
        img_path, target_size=target_size)
    array = keras.utils.img_to_array(img)
    array = numpy.expand_dims(array, axis=0)
    return array

if __name__ == '__main__':
    # Build a ResNet50V2 model loaded with pre-trained ImageNet weights
    model = keras.applications.ResNet50V2(weights="imagenet")
    model.summary()
    print(len(model.layers))

    img_path = keras.utils.get_file(
        fname='cat.jpg',
        origin='https://img-datasets.s3.amazonaws.com/cat.jpg')
    img_tensor = get_img_array(img_path, target_size=(224, 224))
    print(img_tensor.shape)

    predictions = model.predict(keras.applications.resnet_v2.preprocess_input(img_tensor.copy()))
    decoded_predictions = keras.applications.resnet_v2.decode_predictions(predictions, top=3)[0]
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i+1}: {label} ({score:.2f})")

    pyplot.axis('off')
    pyplot.imshow(img_tensor[0].astype('uint8'))
    pyplot.subplots_adjust(left=0, right=1.0, top=0.95, bottom=0.05)
    pyplot.savefig('temp/cat.jpg', dpi=300)
    pyplot.show()
    pyplot.close('all')

    layer_outputs = []
    layer_names = []
    for layer in model.layers:
        if isinstance(layer, (keras.layers.Conv2D)):
            layer_outputs.append(layer.output)
            layer_names.append(layer.name)

    activation_model = keras.Model(inputs=model.input, outputs=layer_outputs)
    activations = activation_model.predict(img_tensor)
    first_layer_activation = activations[0]
    print(first_layer_activation.shape)
    pyplot.matshow(first_layer_activation[0, :, :, 5], cmap='viridis')
    pyplot.subplots_adjust(left=0, right=1.0, top=1.0, bottom=0)
    pyplot.savefig('temp/first_layer_activation.png', dpi=300)
    pyplot.show()
    pyplot.close('all')

    images_per_row = 16
    for layer_name, layer_activation in zip(layer_names, activations):
        n_features = layer_activation.shape[-1]
        size = layer_activation.shape[1]
        n_cols = n_features // images_per_row
        display_grid = numpy.zeros(((size + 1) * n_cols - 1,
                                    images_per_row * (size + 1) - 1))
        for col in range(n_cols):
            for row in range(images_per_row):
                channel_index = col * images_per_row + row
                channel_image = layer_activation[0, :, :, channel_index].copy()
                if channel_image.sum() != 0:
                    channel_image -= channel_image.mean()
                    channel_image /= channel_image.std()
                    channel_image *= 64
                    channel_image += 128
                channel_image = numpy.clip(channel_image, 0, 255).astype('uint8')
                display_grid[
                    col * (size + 1) : (col + 1) * size + col,
                    row * (size + 1) : (row + 1) * size + row] = channel_image
        
        scale = 1. / size
        pyplot.figure(figsize=(scale * display_grid.shape[1],
                               scale * display_grid.shape[0]))
        pyplot.title(layer_name, size=24)
        pyplot.grid(False)
        pyplot.axis('off')
        pyplot.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.1)
        pyplot.imshow(display_grid, aspect='auto', cmap='viridis')
        pyplot.savefig('temp/' + layer_name + '.png', dpi=72)
        # pyplot.show()
        pyplot.close('all')
