import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    # Create a figure containing a single Axes.
    fig, ax = pyplot.shubplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    pyplot.show()

    numpy.random.seed(19680801)
    data = {
        'a': numpy.arange(50),
        'c': numpy.random.randint(0, 50, 50),
        'd': numpy.random.randn(50)
    }
    data['b'] = data['a'] + 10 * numpy.random.randn(50)
    data['d'] = numpy.abs(data['d']) * 100
    fig, ax = pyplot.subplot(figsize=(5, 2.7), layout='constrained')
    ax.scatter('a', 'b', c='c', s='d', data=data)
    ax.set_xlabel('entry a')
    ax.set_ylabel('entry b')
    pyplot.show()
