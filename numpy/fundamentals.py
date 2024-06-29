import matplotlib
import matplotlib.colors
import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    # 1. Array creation
    # Converting Python sequences to NumPy arrays.
    a1d = numpy.array([1, 2, 3, 4])
    a2d = numpy.array([[1, 2], [3, 4]])
    a3d = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=int)

    # 1D array creation functions
    print(numpy.arange(2, 15, 2))
    print(numpy.linspace(2, 15, 3))

    # 2D array creation functions
    print(numpy.eye(3, 5))
    print(numpy.diag([1, 2, 3]))
    print(numpy.diag(numpy.array([[1, 2, 3], [4, 5, 6]])))

    # general ndarray creation functions
    print(numpy.zeros((2, 3)))
    print(numpy.ones((2, 4)))

    print(numpy.random.default_rng(42).random((2, 3)))

    numpy.random.seed(42)
    mean1 = [1, 2]
    cov1 = [[1, 0.5], [0.5, 1]]
    mean2 = [6, 4]
    cov2 = [[2, 1], [1, 2]]
    num_samples_per_group = 200
    sample_group1 = numpy.random.multivariate_normal(mean1, cov1, num_samples_per_group)
    sample_group2 = numpy.random.multivariate_normal(mean2, cov2, num_samples_per_group)
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.06)
    pyplot.scatter(numpy.array(sample_group1)[:, 0],
                   numpy.array(sample_group2)[:, 1], c='green', s=40)
    pyplot.scatter(numpy.array(sample_group2)[:, 0],
                   numpy.array(sample_group2)[:, 1], c='red', s=40)
    pyplot.savefig('image.png', dpi=300)
    pyplot.show()

    a = numpy.array([1, 2, 3, 4, 5, 6])
    b = a[:2]
    b += 1
    print('a =', a, 'b =', b)

    a = numpy.array([1, 2, 3, 4, 5, 6])
    b = a[:2].copy()
    b += 1
    print('a =', a, '; b=', b)

    A = numpy.ones((2, 2))
    B = numpy.eye(2, 2)
    C = numpy.zeros((2, 2))
    D = numpy.diag((-3, -4))
    E = numpy.block([[A, B], [C, D]])
    print(E)

    # 2. Indexing on ndarrays.
    x = numpy.arange(10)
    print(x[2])
    print(x[-2])

    # now x is 2-dimensional
    x.shape =(2, 5)
    print(x[1, 3])
    print(x[1, -1])
    print(x[0])
    print(x[0][2])
