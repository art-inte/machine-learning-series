import keras
import tensorflow

# The dimensions of our input image.
img_width = 360
img_height = 360

# Target layer: we will visualize the filters from this layer.
# See model.summary() for list of layer names, if you want to change this.
layer_name = 'conv3_block4_out'
flower_path = 'res/flower.jpeg'

if __name__ == '__main__':
    # Build a ResNet50V2 model loaded with pre-trained ImageNet weights.
    model = keras.applications.ResNet50V2(weights='imagenet', include_top=False)

    # Set up a model taht returns the activation values for target layer.
    layer = model.get_layer(name=layer_name)
    feature_extractor = keras.Model(inputs=model.inputs, outputs=layer.output)

    def compute_loss(input_image, filter_index):
        activation = feature_extractor(input_image)
        # Avoid border artifacts by only involving non-border pixels in the loss.
        filter_activation = activation[:,2:-2,2:-2, filter_index]
        return tensorflow.reduce_mean(filter_activation)
    
    @tensorflow.function
    def gradient_ascent_step(img, filter_index, learning_rate):
        with tensorflow.GradientTape() as tape:
            tape.watch(img)
            loss = compute_loss(img, filter_index)
        # compute gradients
        grads = tape.gradient(loss, img)
        # normalize gradients
        grads = tensorflow.math.l2_normalize(grads)
        img += learning_rate * grads
        return loss, img

    def initialize_image():
        image_string = tensorflow.io.read_file(flower_path)
        image_decoded = tensorflow.image.decode_jpeg(image_string, channels=3)
        image_shape = tensorflow.shape(image_decoded)
        offset_height = (image_shape[0] - img_height) // 2
        offset_width = (image_shape[1] - img_width) // 2
        image_cropped = tensorflow.image.crop_to_bounding_box(image_decoded,
                                                           offset_height,
                                                           offset_width,
                                                           img_height,
                                                           img_width)
        image_normalized = tensorflow.image.convert_image_dtype(image_cropped, tensorflow.float32)
        image_batch = tensorflow.expand_dims(image_normalized, axis=0)
        return (image_batch - 0.5) * 0.25
 
    def visualize_filter(img, filter_index):
        learning_rate = 5.0
        for _ in range(30):
            loss, img = gradient_ascent_step(img, filter_index, learning_rate)
        return loss, img

    input = initialize_image()
    keras.utils.save_img('temp/convnets_input.png', input[0])
    loss, img = visualize_filter(input, 10)
    img = img[:, 25:-25, 25:-25, :]
    keras.utils.save_img('temp/convnets_filter_response.png', img[0])
