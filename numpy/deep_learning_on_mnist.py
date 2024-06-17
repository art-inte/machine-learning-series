import gzip
import matplotlib.pyplot
import numpy
import os
import requests

data_sources = {
    'training_images': 'train-images-idx3-ubyte.gz',    # 60,000 training images
    'test_images': 't10k-images-idx3-ubyte.gz',         # 10,000 test images
    'training_labels': 'train-labels-idx1-ubyte.gz',    # 60,000 training labels
    'test_labels': 't10k-labels-idx1-ubyte.gz',         # 10,000 test labels
}

# If you encounter downloading problems, you can switch to a different URL.
# base_url = 'http://yann.lecun.com/exdb/mnist/'
base_url = "https://github.com/rossbar/numpy-tutorial-data-mirror/raw/main/"

data_dir = 'temp/mnist/'

def one_hot_encoding(labels, dimension=10):
    # Define a one-hot variable for an all-zero vector
    # with 10 dimensions (number labels from 0 to 9)
    one_hot_labels = labels[..., None] == numpy.arange(dimension)[None]
    # Return one-hot encoded labels
    return one_hot_labels.astype(numpy.float64)

if __name__ == '__main__':
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for filename in data_sources.values():
        file_path = os.path.join(data_dir, filename)
        if not os.path.exists(file_path):
            print('Downloading file: ' + filename)
            resp = requests.get(base_url + filename, stream=True)
            resp.raise_for_status() # ensure download was successful
            with open(file_path, 'wb') as fp:
                for chunk in resp.iter_content(chunk_size=128):
                    fp.write(chunk)

    mnist_dataset = {}

    # images
    for key in ('training_images', 'test_images'):
        with gzip.open(os.path.join(data_dir, data_sources[key]), 'rb') as mnist_file:
            mnist_dataset[key] = numpy.frombuffer(
                mnist_file.read(), numpy.uint8, offset=16
            ).reshape(-1, 28 * 28)

    # labels
    for key in ('training_labels', 'test_labels'):
        with gzip.open(os.path.join(data_dir, data_sources[key]), 'rb') as mnist_file:
            mnist_dataset[key] = numpy.frombuffer(mnist_file.read(), numpy.uint8, offset=8)

    x_train, y_train, x_test, y_test = (
        mnist_dataset['training_images'],
        mnist_dataset['training_labels'],
        mnist_dataset['test_images'],
        mnist_dataset['test_labels'],
    )

    print('The shape of training images: {} and training labels: {}'.format(
            x_train.shape, y_train.shape))
    
    print('The shape of test images: {} and test labels: {}'.format(
        x_test.shape, y_test.shape))

    # Take the 60,000th image (indexed at 59,000) from the training set,
    # reshape from (784,) to (28, 28) to have a valid shape for displaying purposes.
    mnist_image = x_train[59999, :].reshape(28, 28)
    # Set the color mapping to grayscale to have a black background.
    matplotlib.pyplot.imshow(mnist_image, cmap='gray')
    # Display the images.
    matplotlib.pyplot.show()

    # Display 5 random images from the training set.
    num_examples = 5
    rng = numpy.random.default_rng(seed=1)

    fig, axes = matplotlib.pyplot.subplots(nrows=1, ncols=num_examples)
    for sample, ax in zip(rng.choice(x_train, size=num_examples, replace=False), axes):
        ax.imshow(sample.reshape(28, 28), cmap='gray')
    matplotlib.pyplot.show()

    # Display the label of the 60,000th image (indexed at 59,999) from the training set.
    print('The label of the 60,000th train image: ' + str(y_train[59999]))

    print('The data type of training images: {}'.format(x_train.dtype))
    print('The data type of test images: {}'.format(x_test.dtype))

    training_sample, test_sample = 60000, 10000
    training_images = x_train[0:training_sample] / 255.0
    test_images = x_test[0:test_sample] / 255.0

    print('The data type of training images: {}'.format(training_images.dtype))
    print('The data type of test images: {}'.format(test_images.dtype))

    print('The data type of training labels: {}'.format(y_train.dtype))
    print('The data type of test labels: {}'.format(y_test.dtype))

    training_labels = one_hot_encoding(y_train[0:training_sample])
    test_labels = one_hot_encoding(y_test[0:test_sample])

    print('The data type of training labels: {}'.format(training_labels.dtype))
    print('The data type of test labels: {}'.format(test_labels.dtype))

    print('One-hot encoded label for the first training sample: ' + str(training_labels[0]))
