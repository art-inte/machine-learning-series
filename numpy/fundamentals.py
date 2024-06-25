import numpy

if __name__ == '__main__':
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
