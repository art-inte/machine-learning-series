import matplotlib.pyplot as pyplot
import numpy

# Define loss function.
def loss(x, y):
    return (x + y)**2

# Compute the gradient
def gradient(x, y):
    return numpy.array([2*x, 2*y])

# gradient descent parameters
learning_rate = 0.1
max_iter = 100
tolerance=1e-6

if __name__ == '__main__':
    # starting point
    x, y = 3.0, 4.0
    trajectory  = [(x, y)]

    for _ in range(max_iter):
        grad = gradient(x, y)
        x_new, y_new = x - learning_rate * grad[0], y - learning_rate * grad[1]
        trajectory.append((x_new, y_new))

        if numpy.linalg.norm([x_new - x, y_new - y]) < tolerance:
            break

        x, y = x_new, y_new
    
    # Plot the loss surface
    x, y = numpy.meshgrid(numpy.linspace(-5, 5, 100), numpy.linspace(-5, 5, 100))
    z = loss(x, y)

    fig = pyplot.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

    trajectory = numpy.array(trajectory)
    z_trajectory = loss(trajectory[:, 0], trajectory[:, 1])
    ax.plot(trajectory[:, 0], trajectory[:, 1], z_trajectory, 'r.-', markersize=5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    pyplot.subplots_adjust(left=0.05, right=0.95, top=0.96, bottom=0.04)
    pyplot.savefig('temp/visual_gradient_descent.png', dpi=300)
    pyplot.show()
