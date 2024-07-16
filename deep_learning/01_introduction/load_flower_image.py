import keras
import matplotlib.pyplot as pyplot
import pathlib
import tensorflow

dataset_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'

if __name__ == '__main__':
    print(tensorflow.__version__)
    archive = keras.utils.get_file(origin=dataset_url, extract=True)
    data_dir = pathlib.Path(archive).with_suffix('')
    train_ds = keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset='training',
        seed=123,
        image_size=(180, 180),
        batch_size=32)
    class_names = train_ds.class_names
    pyplot.figure(figsize=(10, 10))
    for images, labels in train_ds.take(1):
        for i in range(9):
            ax = pyplot.subplot(3, 3, i + 1)
            pyplot.imshow(images[i].numpy().astype('uint8'))
            pyplot.title(class_names[labels[i]])
            pyplot.axis('off')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.04)
    pyplot.savefig('temp/flower_photos_with_label.png', dpi=300)
    pyplot.show()
    pyplot.close('all')
