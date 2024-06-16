import gzip
import numpy
import os
import requests

data_sources = {
    'training_images': 'train-images-idx3-ubyte.gz',    # 60,000 training images
    'test_images': 't10k-images-idx3-ubyte.gz',         # 10,000 test images
    'training_labels': 'train-labels-idx1-ubyte.gz',    # 60,000 training labels
    'test_labels': 't10k-labels-idx1-ubyte.gz',         # 10,000 test labels
}

# base_url = 'http://yann.lecun.com/exdb/mnist/'
base_url = "https://github.com/rossbar/numpy-tutorial-data-mirror/blob/main/"
data_dir = 'temp/mnist/'

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
