
import numpy
import matplotlib.pyplot as pyplot

def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))

if __name__ == '__main__':
    x = numpy.linspace(-10, 10, 400)
    y = sigmoid(x)
    pyplot.figure(figsize=(8, 6))
    pyplot.plot(x, y, label='Sigmoid function')
    pyplot.title('Sigmoid Function')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.axhline(0, color='black',linewidth=2)
    pyplot.axvline(0, color='red',linewidth=2)
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    pyplot.savefig('temp/sigmoid_function.png', dpi=300)
    pyplot.show()