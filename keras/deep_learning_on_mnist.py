import keras
import matplotlib.pyplot as pyplot
import numpy

epochs = 5

if __name__ == '__main__':
    print('Keras version: ', keras.__version__)

    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # save ppm image
    width, height = 28, 28
    image_data = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    for y in range(height):
            for x in range(width):
                 color = x_train[0][y, x]
                 image_data[y, x] = [color, color, color]
                  
    with open('temp/mnist_first_digit.ppm', 'wb') as file:
        file.write(('P6\n' + str(width) + ' ' + str(height) + ' ' + str(255) + '\n').encode('ascii'))
        file.write(image_data.tobytes())

    # Create a figure and axis
    fig, ax = pyplot.subplots(figsize=(10, 10))
    grid = numpy.arange(1, width*height + 1).reshape((height, width))
    for i in range(height):
         for j in range(width):
              ax.text(j, height - i - 1, str(x_train[0][i, j]), va='center', ha='center', fontsize=8)
    ax.set_xticks(numpy.arange(-0.5, width, 1), minor=True)
    ax.set_yticks(numpy.arange(-0.5, height, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(which='major', bottom=False, left=False, labelbottom=False, labelleft=False)
    pyplot.show()


    x_train, x_test = x_train / 255.0, x_test / 255.0

    print('Shape of train image:', x_train.shape)
    print('Shape of test image:', x_test.shape)

    model = keras.models.Sequential([
        keras.layers.Input(shape=(28, 28)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.summary()

    loss_fn = keras.losses.SparseCategoricalCrossentropy()

    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs)

    model.evaluate(x_test, y_test, verbose=2)

    predictions = numpy.argmax(model.predict(x_test[:5]), axis=1)
    print("Predictions: " + str(predictions), ", Labels: " + str(y_test[:5]))
