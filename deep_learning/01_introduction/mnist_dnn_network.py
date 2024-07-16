import keras
import matplotlib.pyplot as pyplot
import networkx
import numpy

epochs = 5

if __name__ == '__main__':
    print('Keras version: ', keras.__version__)
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # save ppm image
    scale = 10
    width, height = 28, 28
    image_data = numpy.zeros((height * scale, width * scale, 3), dtype=numpy.uint8)
    for y in range(height):
            for x in range(width):
                 color = x_train[0][y, x]
                 for s in range(scale):
                    for c in range(scale):
                        image_data[y * scale + s, x * scale + c] = [color, color, color]

    with open('temp/mnist_first_digit.ppm', 'wb') as file:
        file.write(('P6\n' + str(width * scale) + ' ' + 
                    str(height * scale) + ' ' + str(255) + '\n').encode('ascii'))
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
    # Remove major ticks.
    ax.tick_params(which='major', bottom=False, left=False, labelbottom=False, labelleft=False)
    # Remove minor ticks on the bottom and left.
    ax.tick_params(which='minor', bottom=False, left=False)
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.04)
    pyplot.savefig('temp/number_with_digit_show.png', dpi=300)
    pyplot.show()
    pyplot.close('all')

    x_train, x_test = x_train / 255.0, x_test / 255.0

    print('Shape of train image:', x_train.shape)
    print('Shape of test image:', x_test.shape)

    model = keras.models.Sequential([
        keras.layers.Input(shape=(28, 28)),
        keras.layers.Flatten(),
        keras.layers.Dense(48, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.summary()

    layer_units = [layer.units for layer in model.layers
                    if isinstance(layer, keras.layers.Dense)]
    graph = networkx.DiGraph()
    # Add nodes for each layer.
    for i, size in enumerate(layer_units):
         for j in range(size):
              graph.add_node(f'L{i+1}_{j}', layer=i)
    # Add edges between layers.
    for i in range(len(layer_units) - 1):
         for j in range(layer_units[i]):
              for k in range(layer_units[i+1]):
                   graph.add_edge(f'L{i+1}_{j}', f'L{i+2}_{k}')
    # Get positions for the nodes in each layer.
    largest = numpy.max(layer_units)
    pos = {}
    for i, size in enumerate(layer_units):
         x = [i] * size
         y = range(size)
         scale = largest / size
         pos.update({f'L{i+1}_{j}': (x[j], y[j] * scale) for j in range(size)})
    # Width and height in inches.
    fig, ax = pyplot.subplots(figsize=(16, 9))
    pyplot.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0)
    # Draw the nodes.
    networkx.draw_networkx_nodes(graph, pos, node_size=60, node_color='skyblue', ax=ax)
    # Draw the edges.
    networkx.draw_networkx_edges(graph, pos, edge_color='gray', width=0.1, arrows=False, ax=ax)
    labels = {f'L{len(layer_units)-1}_{j}': f'{j}' for j in range(layer_units[-1])}
    label_pos = {f'L{len(layer_units)-1}_{j}': (x[j] + 0.1, y[j] * scale) for j in range(size)}
    networkx.draw_networkx_labels(graph, label_pos, labels, font_size=12, font_color='blue', ax=ax)
    ax.axis('off')

    loss_fn = keras.losses.SparseCategoricalCrossentropy()
    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=epochs)

    model.evaluate(x_test, y_test, verbose=2)

    predictions = numpy.round(model.predict(x_train[:1]), 3)
    print(predictions)
    predict_labels = {f'L{len(layer_units)-1}_{j}': predictions[0][j] for j in range(layer_units[-1])}
    predict_pos = {f'L{len(layer_units)-1}_{j}': (x[j], y[j] * scale) for j in range(size)}
    networkx.draw_networkx_labels(graph, predict_pos, predict_labels, font_size=12, ax=ax)
    pyplot.savefig('temp/mnist_dnn_graph.png', dpi=300)
    pyplot.show()
    pyplot.close('all')

    layers_name = ['dense', 'dense_1', 'dense_2', 'dense_3']

    for name in layers_name:
        layer = model.get_layer(name=name)
        pyplot.figure(figsize=(10, 4))
        weights, biases = layer.get_weights()
        print(weights.shape)
        n_column = 12
        n_row = int(numpy.ceil(weights.shape[1] / n_column))
        for i in range(weights.shape[1]):
            ax = pyplot.subplot(n_row, n_column, i+1)
            sqrt_n = numpy.sqrt(len(weights[:, i])).astype(int)
            factor1 = 1
            factor2 = 1
            for i in range(sqrt_n, 0, -1):
                if len(weights[:, i]) % i == 0:
                    factor1 = i
                    factor2 = len(weights[:, i]) // i
                    break
            weight_image = weights[:, i].reshape(factor1, factor2)
            pyplot.imshow(weight_image, cmap='gray')
            pyplot.axis('off')
        pyplot.show()
        pyplot.close('all')

    predictions = numpy.argmax(model.predict(x_test[:5]), axis=1)
    print("Predictions: " + str(predictions), ", Labels: " + str(y_test[:5]))
