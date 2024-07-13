import keras
import matplotlib.pyplot as pyplot
import numpy

class WeightHistory(keras.callbacks.Callback):
    def __init__(self):
        super(WeightHistory, self).__init__()
        self.current_epoch = 0

    def on_epoch_begin(self, epoch, logs={}):
        self.current_epoch = epoch

    def on_train_batch_end(self, batch, logs={}):
        weights, biases = self.model.layers[0].get_weights()
        print('Epoches {} Batch {}: Weights = {}, Biases = {}'
                .format(self.current_epoch, batch + 1, weights, biases))

    def on_epoch_end(self, epoch, logs={}):
        weights, biases = self.model.layers[0].get_weights()
        # print('Epoch {}: Weights = {}, Biases = {}'.format(epoch + 1, weights, biases))

        filename = str(epoch) + '.png'
        pyplot.scatter(input[:, 0], input[:, 1], c=output, cmap='bwr')
        x1_vars = numpy.linspace(-3, 3, 100)
        x2_vars = 0 if weights[1] == 0 else -(weights[0] * x1_vars + biases[0]) / weights[1]
        pyplot.plot(x1_vars, x2_vars, label='Decision Boundary')
        pyplot.savefig('temp/' + filename, dpi=300)
        pyplot.clf()

if __name__ == '__main__':
    numpy.random.seed(0)
    input = numpy.random.randn(90, 2)
    output = numpy.array([1 if x + y > 0 else 0 for x, y in input])
    pyplot.scatter(input[:, 0], input[:, 1], c=output, cmap='bwr')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.06)
    pyplot.savefig('temp/random_points_binary_classify.png', dpi=300)
    pyplot.show()

    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(2,)))
    model.add(keras.layers.Dense(1, activation='sigmoid',
            kernel_initializer=keras.initializers.Constant(value=0),
            bias_initializer=keras.initializers.Constant(value=1.0)))
    model.summary()

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    weight_history = WeightHistory()
    model.fit(input, output, epochs=10, batch_size=1, verbose=2, callbacks=[weight_history])
