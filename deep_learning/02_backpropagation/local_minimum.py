import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    x = numpy.linspace(-2, 4 * numpy.pi, 1000)
    y = x * numpy.sin(x)

    pyplot.figure(figsize=(8, 6))
    pyplot.plot(x, y, label='x * sin(x)')
    pyplot.grid(True)
    pyplot.legend()
    pyplot.subplots_adjust(left=0.08, right=0.92, top=0.96, bottom=0.06)
    pyplot.savefig('temp/local_minimum.png', dpi=300)
    pyplot.show()
