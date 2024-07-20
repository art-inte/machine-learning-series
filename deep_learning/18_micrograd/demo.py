import matplotlib.pyplot as pyplot
import network
import numpy
import random
if __name__ == '__main__':
    numpy.random.seed(1337)
    # 2-layer neural network
    model = network.MLP(2, [16, 16, 1])
    print(model)
    print('Number of parameters', len(model.parameters()))
