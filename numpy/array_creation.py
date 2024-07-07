import matplotlib
import matplotlib.colors
import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    # Converting Python sequences to NumPy arrays.
    a1d = numpy.array([1, 2, 3, 4])
    print('1D array:', a1d)
    a2d = numpy.array([[1, 2], [3, 4]])
    print('2D array:', numpy.array_str(a2d).replace('\n', ''))
    a3d = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=int)
    print('3D array:', numpy.array_str(a3d).replace('\n', ''))

    print('Numpy default type:', a1d.dtype)

    print(numpy.arange(10))
    print(numpy.arange(2, 10, dtype=float))
    print(numpy.arange(2, 3, 0.1))

    print(numpy.linspace(0, 5, 5))
    print(numpy.linspace(0, 1, 10, endpoint=False))
    # draw sin function
    x = numpy.linspace(0, 2 * numpy.pi, 200)
    y = numpy.sin(x)
    pyplot.plot(x, y)
    pyplot.subplots_adjust(left=0.1, right=0.9, top=0.92, bottom=0.06)
    pyplot.title('Plot of sin(x)')
    pyplot.savefig('temp/draw_sin_with_linspace.png', dpi=300)
    pyplot.show()

    # 2D array creation functions
    print(numpy.eye(3, 5))
    print(numpy.diag([1, 2, 3]))
    print(numpy.diag(numpy.array([[1, 2, 3], [4, 5, 6]])))
    
    print(numpy.vander((2, 4, 7, 9), 4))

    # general ndarray creation functions
    print(numpy.zeros((2, 3)))
    print(numpy.ones((2, 4)))

    default_rng = numpy.random.default_rng(42)
    print(default_rng.random((2, 3)))
    # retain 3 decimal places
    print(numpy.round(default_rng.random((2, 5)), 3))

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
