import keras
import numpy
if __name__ == '__main__':
    print(keras.__version__)
    balls = numpy.array([[1], [8], [3], [10], [4], [12], [6], [13]])
    colors = numpy.array([0, 1, 0, 1, 0, 1, 0, 1])
    predicts = numpy.array([[4], [5], [9]])

    model = keras.Sequential([
        keras.layers.Input(shape=(1,)),
        keras.layers.Dense(1, activation='sigmoid')])

    model.compile(loss='binary_crossentropy',
        optimizer=keras.optimizers.Adam(learning_rate=1.0),
        metrics=['accuracy'])

    model.fit(balls, colors, epochs=10, batch_size=1)

    print(model.predict(predicts))
