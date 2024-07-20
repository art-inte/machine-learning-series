import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    x = numpy.linspace(-5, 5, 400)
    y1 = numpy.power(x, 4) - 2 * numpy.power(x, 2) - 3
    y2 = numpy.power(x, 3) - 4 * x

    fig, (ax1, ax2) = pyplot.subplots(1, 2)
    ax1.plot(x, y1)
    ax2.plot(x, y2)
    pyplot.tight_layout()
    pyplot.subplots_adjust(left=0.08, right=0.92, top=0.96, bottom=0.06)
    pyplot.savefig('temp/function_symmetry.png', dpi=300)
    pyplot.show()
