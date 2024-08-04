import keras
import numpy
from jax import jit, grad, random

if __name__ == '__main__':
    rng = random.key(0)

    batch_size = 128

    (train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
    num_train = train_images.shape[0]
    print('Number of train images is ', num_train)

    num_complete_batches, leftover = divmod(num_train, batch_size)
    num_batches = num_complete_batches + bool(leftover)

    def data_stream():
        rng = numpy.random.RandomState(0)
        while True:
            perm = rng.permutation(num_train)
            for i in range(num_batches):
                batch_idx = perm[i * batch_size:(i + 1) * batch_size]
                yield train_images[batch_idx], train_labels[batch_idx]
    batches = data_stream()
