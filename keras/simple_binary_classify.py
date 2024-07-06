import keras
import matplotlib.pyplot as pyplot
import numpy

if __name__ == '__main__':
    numpy.random.seed(0)
    input = numpy.random.randn(200, 2)
    output = numpy.array([1 if x + y > 0 else 0 for x, y in input])
    pyplot.scatter(input[:, 0], input[:, 1], c=output, cmap='bwr')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.06)
    pyplot.savefig('temp/random_points_binary_classify.png', dpi=300)
    pyplot.show()

    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(2,)))
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(input, output, epochs=100, batch_size=1, verbose=2)

    weights, biases = model.layers[0].get_weights()
    w1, w2 = weights[:, 0]
    b = biases[0]

    pyplot.scatter(input[:, 0], input[:, 1], c=output, cmap='bwr')
    x1_vars = numpy.linspace(-3, 3, 100)
    x2_vars = -(w1 * x1_vars + b) / w2

    pyplot.plot(x1_vars, x2_vars, label='Decision Boundary')
    pyplot.show()
