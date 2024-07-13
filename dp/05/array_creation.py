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
    pyplot.clf()

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

    indices = numpy.indices((3, 3))
    print(numpy.array_str(indices).replace('\n', ''))

    # Generate a 2D grid of indices with shape (100, 100).
    x, y = numpy.indices((100, 100))
    distance = numpy.sqrt((x - 50)**2 + (y - 50)**2)
    pyplot.imshow(distance, cmap='viridis')
    pyplot.colorbar()
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.06)
    pyplot.savefig('temp/colorbar_with_indices.png', dpi=300)
    pyplot.show()
    pyplot.clf()

    a = numpy.array([1, 2, 3, 4, 5, 6])
    b = a[:2]
    b += 1
    print('a =', a, 'b =', b)

    a = numpy.array([1, 2, 3, 4, 5, 6])
    b = a[:2].copy()
    b += 1
    print('a =', a, 'b =', b)

    c = numpy.ones((2, 2))
    d = numpy.eye(2, 2)
    e = numpy.zeros((2, 2))
    f = numpy.diag((-3, -4))
    g = numpy.block([[c, d], [e, f]])
    print(g)
