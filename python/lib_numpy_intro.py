import matplotlib.pyplot as pyplot
import numpy
import pandas

if __name__ == '__main__':
    # 1. NumPy: the absolute basics for beginners.
    a = numpy.array([1, 2, 3, 4, 5, 6])
    print(a)
    print(a[0])
    a[0] = 10
    print(a)
    print(a[:3])

    b = a[3:]
    print(b)
    b[0] = 40
    print(a)

    a = numpy.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]])
    print(a)
    print(a[1, 3])

    print(a.ndim)
    print(a.shape)
    print(a.size)
    print(a.dtype)

    print(numpy.zeros(2))
    print(numpy.ones(2))
    print(numpy.arange(4))
    print(numpy.arange(2, 9, 2))
    print(numpy.linspace(0, 10, num=5))
    print(numpy.ones(2, dtype=numpy.int64))

    arr = numpy.array([2, 1, 5, 3, 7, 4, 6, 8])
    numpy.sort(arr)
    print(arr)

    a = numpy.array([1, 2, 3, 4])
    b = numpy.array([5, 6, 7, 8])
    print(numpy.concatenate((a, b)))
    x = numpy.array([[1, 2], [3, 4]])
    y = numpy.array([[5, 6]])
    print(numpy.concatenate((x, y), axis=0))

    gender_dataset = pandas.read_csv('res/gender_height_weight.csv')

    data = []
    y_trues = []
    for index, row in gender_dataset.iterrows():
        data.append(numpy.array([row['Height'], row['Weight']]))
        y_trues.append(1 if row['Gender'] == 'Male' else 0)

    # A scatter plot of y vs. x with varying marker size and/or color.
    pyplot.scatter(numpy.array(data)[:, 0], numpy.array(data)[:, 1], c=y_trues)
    pyplot.show()
