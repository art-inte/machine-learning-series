import numpy
import matplotlib.pyplot as pyplot
import tensorflow_datasets as tfds


if __name__ == '__main__':
    ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
    fig = tfds.show_examples(ds, ds_info)
