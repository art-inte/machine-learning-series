import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import numpy

def quandratic(x):
    return x**2

def derivative(x):
    return 2*x

if __name__ == '__main__':
    x = numpy.linspace(-10, 10, 400)

    fig, ax = pyplot.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-5, 100)
    line1, = ax.plot(x, quandratic(x), label='f(x) = x^2')
    tangent_line, = ax.plot([], [], label='Tangent line', color='red')
    point, = ax.plot([], [], 'ro')



    def init():
        tangent_line.set_data([], [])
        point.set_data([], [])
        return tangent_line, point

    def update(frame):
        x0 = x[frame]
        y = quandratic(x0)
        slope = derivative(x0)
        x_tangent = numpy.linspace(x0 - 3, x0 + 3, 100)
        y_tangent = slope * (x_tangent - x0) + y
        tangent_line.set_data(x_tangent, y_tangent)
        point.set_data(x0, y)
        return tangent_line, point

    ani = animation.FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)
    pyplot.show()
