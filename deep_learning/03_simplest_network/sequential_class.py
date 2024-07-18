import keras
import matplotlib.pyplot as pyplot
import networkx
import numpy

if __name__ == '__main__':
    model = keras.Sequential()
    model.add(keras.layers.Dense(12))
    model.add(keras.layers.Dense(8))
    model.add(keras.layers.Dense(4))
    model.add(keras.layers.Dense(2))
    model.build((None, 16))
    model.summary()

    layer_units = [layer.units for layer in model.layers]
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
         size = size + 1
         x = [i] * size
         y = range(size)
         scale = largest / size
         pos.update({f'L{i+1}_{j}': (x[j], (y[j] + 0.5) * scale) for j in range(size)})
    # Width and height in inches.
    fig, ax = pyplot.subplots(figsize=(8, 5))
    pyplot.subplots_adjust(left=0.0, right=1.0, top=0.99, bottom=0.01)
    # Draw the nodes.
    networkx.draw_networkx_nodes(graph, pos, node_size=100, node_color='skyblue', ax=ax)
    # Draw the edges.
    networkx.draw_networkx_edges(graph, pos, edge_color='gray', width=0.3, arrows=False, ax=ax)
    ax.axis('off')
    pyplot.savefig('temp/sequential_class.png', dpi=150)
    pyplot.show()
    pyplot.close('all')
