import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    x = numpy.linspace(-5, 5, 1000)
    y = 1 / numpy.sqrt(2 * numpy.pi) * numpy.exp(-0.5 * x**2)

    pyplot.plot(x, y, label='Standard Normal Distribution')
    pyplot.savefig('temp/standard_normal_distribution.png', dpi=300)
    pyplot.show()
