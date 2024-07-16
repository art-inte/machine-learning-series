import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    x = numpy.linspace(-5, 7, 400)
    y = (2 * x - 2) ** 2

    pyplot.plot(x, y, label='f(x) = (2x - 2)^2')

    x = numpy.ones((400, ))
    y = numpy.linspace(-10, 100, 400)
    pyplot.plot(x, y)

    x = [4]
    y = [(2 * 4 - 2) ** 2]
    pyplot.scatter(x, y, color='red', marker='o', s=50, label='(4, 36)')
    pyplot.legend()
    pyplot.subplots_adjust(left=0.08, right=0.92, top=0.96, bottom=0.06)
    pyplot.savefig('temp/quadratic_curve.png', dpi=300)
    pyplot.show()
