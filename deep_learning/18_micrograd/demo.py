import matplotlib.pyplot as pyplot
import network
import numpy
from sklearn.datasets import make_moons
if __name__ == '__main__':
    numpy.random.seed(1337)
    X, y = make_moons(n_samples=100, noise=0.1)
    # make y be -1 or 1
    y = y * 2 - 1
    # visualize in 2D
    pyplot.figure(figsize=(10, 10))
    pyplot.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
    pyplot.tick_params(axis='both', which='major', labelsize=24)
    pyplot.scatter(X[:, 0], X[:, 1], c=y, s=200, cmap='jet')
    pyplot.savefig('make_moons.png')

    # 2-layer neural network
    model = network.MLP(2, [16, 16, 1])
    print(model)
    print('Number of parameters', len(model.parameters()))
