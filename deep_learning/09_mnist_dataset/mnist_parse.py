import array
import file_util
import numpy
import struct

"""
THE MNIST DATABASE of handwritten digits

http://yann.lecun.com/exdb/mnist/

The MNIST database of handwritten digits, available from this page, has a training set of
60000 examples, and a test set of 10000 examples.
"""

training_set_images_url = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
training_set_labels_url = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
test_set_images_url = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
test_set_labels_url = 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'

def mnist_read(images_path, labels_path):
    labels = []
    with open(labels_path, 'rb') as file:
        magic, size = struct.unpack('>II', file.read(8))
        if magic != 2049:
            raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
        labels = array.array('B', file.read())

    with open(images_path, 'rb') as file:
        magic, size, rows, cols = struct.unpack('>IIII', file.read(16))
        if magic != 2051:
            raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
        image_data = array.array('B', file.read())

    images = []
    for k in range(size):
        images.append([0] * rows * cols)
    for j in range(size):
        img = numpy.array(image_data[j * rows * cols:(j + 1) * rows * cols])
        img = img.reshape(28, 28)
        images[j][:] = img

    return numpy.array(images), numpy.array(labels)

def mnist_load():
    """
    Loads the MNIST dataset.

    This is a dataset of 60000 28x28 images of along with a test set of 10000 images.

    Returns:

    Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    training_images = file_util.get_file(origin_url=training_set_images_url, extract=True)
    training_labels = file_util.get_file(origin_url=training_set_labels_url, extract=True)
    test_images = file_util.get_file(origin_url=test_set_images_url, extract=True)
    test_labels = file_util.get_file(origin_url=test_set_labels_url, extract=True)

    image_train, label_train = mnist_read(training_images, training_labels)
    image_test, label_test = mnist_read(test_images, test_labels)

    return (image_train, label_train), (image_test, label_test)
