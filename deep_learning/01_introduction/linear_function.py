import numpy
import matplotlib.pyplot as pyplot

if __name__ == '__main__':
    x_points = [0, 2, 5, 7, 9, 7, 7]
    y_points = [4, 10, 19, 25, 31, 18, 32]

    i = numpy.linspace(0, 10, 100)
    o = 3 * i + 4
    pyplot.plot(i, o, label='o = 3 * i + 4')
    pyplot.text(10, 34, 'o = 3 * i + 4')
    o1 = 2 * i + 4
    pyplot.plot(i, o1, label='o1 = 2 * i + 4')
    pyplot.text(10, 24, 'o1 = 2 * i + 4')
    o2 = 4 * i + 4
    pyplot.plot(i, o2, label='o2 = 4 * i + 4')
    pyplot.text(10, 44, 'o2 = 4 * i + 4')
    pyplot.plot(numpy.full(100, 7), numpy.linspace(0, 50, 100))
    pyplot.scatter(x_points, y_points, color='red', label='Points (2,10), (5,19), (9,31)', zorder=5)
    for x, y in zip(x_points, y_points):
        pyplot.text(x, y, f'({x},{y})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    pyplot.grid(True)
    pyplot.subplots_adjust(left=0.06, right=0.85, top=0.96, bottom=0.06)
    pyplot.savefig('res/deep_learning/linear_function.png', dpi=300)
    pyplot.show()
