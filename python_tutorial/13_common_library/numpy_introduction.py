import matplotlib.pyplot as pyplot
import numpy
import pandas

if __name__ == '__main__':
    a = numpy.array([1, 2, 3, 4, 5, 6])
    print(a)
    print(a[0])

    a[0] = 10
    print('Modified index 0', a)
    b = a[3:]
    print('Slice', b)
    b[0] = 40
    print('Modified index 3', a)

    a = numpy.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]])
    print('[Row 1 and column 3]', a[1, 3])

    print('The number of dimensions of an array', a.ndim)
    print('The shape of an array is a tuple', a.shape)
    print('Length of shape == dimensions', len(a.shape) == a.ndim)
    print('The fixed, total number of elements in array', a.size)
    print('The data type is recorded in the dtype attribute', a.dtype)

    print('Zero array', numpy.zeros(2))
    print('One array', numpy.ones(2))
    print('Random array', numpy.empty(2))

    print(numpy.arange(4))
    print(numpy.arange(2, 9, 2))

    print('Linearly in a specified interval', numpy.linspace(0, 10, num=5))

    print(numpy.ones(2, dtype=numpy.int64), 'element dtype is int64')

    b = numpy.array([2, 1, 5, 3, 7, 4, 6, 8])
    print('Sorted', numpy.sort(b))

    c = numpy.array([1, 2, 3, 4])
    d = numpy.array([5, 6, 7, 8])
    print(numpy.concatenate((c, d)))
    e = numpy.array([[1, 2], [3, 4]])
    f = numpy.array([[5, 6]])
    print(numpy.concatenate((e, f), axis=0))
