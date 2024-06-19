import keras
import numpy
import tensorflow as tf
import tensorflow_datasets

epochs = 5

if __name__ == '__main__':
    print('TensorFlow version: ', tf.__version__)

    (x_train, y_train), (x_test, y_test) = tensorflow_datasets.as_numpy(
        tensorflow_datasets.load(
        'mnist',
        split=['train', 'test'],
        batch_size=-1,
        as_supervised=True,
    ))
    x_train, x_test = numpy.squeeze(x_train, axis=3) / 255.0, numpy.squeeze(x_test, axis=3) / 255.0
    print('Shape of train image:', x_train.shape)
    print('Shape of test image:', x_test.shape)

    model = keras.models.Sequential()
    model.add(keras.layers.Input(shape=(28, 28)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dense(10, activation='softmax'))

    loss_fn = keras.losses.SparseCategoricalCrossentropy()

    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs)

    model.evaluate(x_test, y_test, verbose=2)

    predictions = numpy.argmax(model.predict(x_test[:5]), axis=1)
    print("Predictions: " + str(predictions), ", Labels: " + str(y_test[:5]))
