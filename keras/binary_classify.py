import keras
import numpy

class WeightHistory(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        weights, biases = self.model.layers[0].get_weights()
        # print('Epoch {}: Weights = {}, Biases = {}'.format(epoch + 1, weights, biases))

if __name__ == '__main__':
    numpy.random.seed(42)
    mean1 = [1, 2]
    cov1 = [[1, 0.5], [0.5, 1]]
    mean2 = [6, 4]
    cov2 = [[2, 1], [1, 2]]
    num_samples_per_group = 200
    sample_group1 = numpy.random.multivariate_normal(mean1, cov1, num_samples_per_group)
    sample_group2 = numpy.random.multivariate_normal(mean2, cov2, num_samples_per_group)
    print(sample_group1)

    model = keras.Sequential([
        keras.layers.Input(shape=(2,)),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    model.summary()

    weight_history = WeightHistory()

    sample_group = []
    output = []
    for i in range(num_samples_per_group * 2):
        if i % 2 == 0:
            sample_group.append(sample_group1[i // 2])
            output.append(0)
        else:
            sample_group.append(sample_group2[i // 2])
            output.append(1)

    sample_group = numpy.array(sample_group)
    output = numpy.array(output)
    model.fit(sample_group, output, epochs=10, callbacks=[weight_history])

    # model.fit(sample_group1, numpy.zeros(num_samples_per_group), epochs=10, callbacks=[weight_history])
    # model.fit(sample_group2, numpy.ones(num_samples_per_group), epochs=10, callbacks=[weight_history])

    print(model.predict(numpy.array([[1, 2]])))

    weights, biases = model.layers[0].get_weights()
    print('Weights:', weights)
    print('Biases:', biases)
