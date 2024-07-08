import matplotlib.pyplot as pyplot
import numpy
import secrets

if __name__ == '__main__':
    rng = numpy.random.default_rng(0)
    # Generate one random float uniformly distributed over the range [0, 1)
    print(rng.random())
    # Generate an array of 100 numbers according to a unit Gaussian distribution.
    print(numpy.round(rng.standard_normal(10), 3))
    # Generate an array of 5 integers uniformly over the range [0, 10).
    print(rng.integers(low=0, high=10, size=5))
    
    rng = numpy.random.default_rng(secrets.randbits(128))
    print(rng.random())

    numbers = numpy.random.default_rng(0).uniform(low=0.0, high=10.0, size=(400, 2))
    pyplot.scatter(numbers[:, 0], numbers[:, 1])
    pyplot.title('Uniform Random Numbers')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.94, bottom=0.06)
    pyplot.savefig('temp/uniform_random_numbers.png', dpi=300)
    pyplot.show()
    pyplot.clf()

    numbers = numpy.random.default_rng(0).normal(5, 1, size=(400, 2))
    pyplot.scatter(numbers[:, 0], numbers[:, 1])
    pyplot.title('Normal Distribution with mean=5 and std=1')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.94, bottom=0.06)
    pyplot.savefig('temp/normal_distribution_numbers.png', dpi=300)
    pyplot.show()
    pyplot.clf()

    numbers = numpy.random.default_rng(0).standard_normal((400, 2))
    colors = numpy.array([1 if x + y > 0 else 0 for x, y in numbers])
    pyplot.scatter(numbers[:, 0], numbers[:, 1], c=colors, cmap='bwr')
    pyplot.title('Standard Normal with Decision Boundary')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.94, bottom=0.06)
    pyplot.savefig('temp/standard_normal_with_decision_boundary.png', dpi=300)
    pyplot.show()
    pyplot.clf()
