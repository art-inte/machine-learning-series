import gzip
import matplotlib.pyplot
import numpy
import os
import requests

data_sources = {
    'training_images': 'train-images-idx3-ubyte.gz',    # 60,000 training images
    'test_images': 't10k-images-idx3-ubyte.gz',         # 10,000 test images
    'training_labels': 'train-labels-idx1-ubyte.gz',    # 60,000 training labels
    'test_labels': 't10k-labels-idx1-ubyte.gz',         # 10,000 test labels
}

# If you encounter downloading problems, you can switch to a different URL.
# base_url = 'http://yann.lecun.com/exdb/mnist/'
base_url = "https://github.com/rossbar/numpy-tutorial-data-mirror/raw/main/"

data_dir = 'temp/mnist/'

def one_hot_encoding(labels, dimension=10):
    # Define a one-hot variable for an all-zero vector
    # with 10 dimensions (number labels from 0 to 9)
    one_hot_labels = labels[..., None] == numpy.arange(dimension)[None]
    # Return one-hot encoded labels
    return one_hot_labels.astype(numpy.float64)

# Define ReLU that returns the input if it's positive and 0 otherwise.
def relu(x):
    return (x >= 0) * x

# Set up a derivative of the ReLU function that returns 1 for a positive input
# and 0 otherwise.
def relu2deriv(output):
    return output >= 0

if __name__ == '__main__':
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for filename in data_sources.values():
        file_path = os.path.join(data_dir, filename)
        if not os.path.exists(file_path):
            print('Downloading file: ' + filename)
            resp = requests.get(base_url + filename, stream=True)
            resp.raise_for_status() # ensure download was successful
            with open(file_path, 'wb') as fp:
                for chunk in resp.iter_content(chunk_size=128):
                    fp.write(chunk)

    mnist_dataset = {}

    # images
    for key in ('training_images', 'test_images'):
        with gzip.open(os.path.join(data_dir, data_sources[key]), 'rb') as mnist_file:
            mnist_dataset[key] = numpy.frombuffer(
                mnist_file.read(), numpy.uint8, offset=16
            ).reshape(-1, 28 * 28)

    # labels
    for key in ('training_labels', 'test_labels'):
        with gzip.open(os.path.join(data_dir, data_sources[key]), 'rb') as mnist_file:
            mnist_dataset[key] = numpy.frombuffer(mnist_file.read(), numpy.uint8, offset=8)

    x_train, y_train, x_test, y_test = (
        mnist_dataset['training_images'],
        mnist_dataset['training_labels'],
        mnist_dataset['test_images'],
        mnist_dataset['test_labels'],
    )

    print('The shape of training images: {} and training labels: {}'.format(
            x_train.shape, y_train.shape))
    
    print('The shape of test images: {} and test labels: {}'.format(
        x_test.shape, y_test.shape))

    # Take the 60,000th image (indexed at 59,000) from the training set,
    # reshape from (784,) to (28, 28) to have a valid shape for displaying purposes.
    mnist_image = x_train[59999, :].reshape(28, 28)
    # Set the color mapping to grayscale to have a black background.
    matplotlib.pyplot.imshow(mnist_image, cmap='gray')
    # Display the images.
    matplotlib.pyplot.show()

    # Display 5 random images from the training set.
    num_examples = 5
    rng = numpy.random.default_rng(seed=1)

    fig, axes = matplotlib.pyplot.subplots(nrows=1, ncols=num_examples)
    for sample, ax in zip(rng.choice(x_train, size=num_examples, replace=False), axes):
        ax.imshow(sample.reshape(28, 28), cmap='gray')
    matplotlib.pyplot.show()

    # Display the label of the 60,000th image (indexed at 59,999) from the training set.
    print('The label of the 60,000th train image: ' + str(y_train[59999]))

    print('The data type of training images: {}'.format(x_train.dtype))
    print('The data type of test images: {}'.format(x_test.dtype))

    training_sample, test_sample = 60000, 10000
    training_images = x_train[0:training_sample] / 255.0
    test_images = x_test[0:test_sample] / 255.0

    print('The data type of training images: {}'.format(training_images.dtype))
    print('The data type of test images: {}'.format(test_images.dtype))

    print('The data type of training labels: {}'.format(y_train.dtype))
    print('The data type of test labels: {}'.format(y_test.dtype))

    training_labels = one_hot_encoding(y_train[0:training_sample])
    test_labels = one_hot_encoding(y_test[0:test_sample])

    print('The data type of training labels: {}'.format(training_labels.dtype))
    print('The data type of test labels: {}'.format(test_labels.dtype))

    print('One-hot encoded label for the first training sample: ' + str(training_labels[0]))

    learning_rate = 0.005
    epochs = 20
    hidden_size = 100
    pixels_per_images = 784
    num_labels = 10

    weights_1 = 0.2 * rng.random((pixels_per_images, hidden_size)) - 0.1
    weights_2 = 0.2 * rng.random((hidden_size, num_labels)) - 0.1

    # To store training and test set losses and accurate predictions
    # for visualization.
    store_training_loss = []
    store_training_accurate_pred = []
    store_test_loss = []
    store_test_accurate_pred = []

    # This is a training loop.
    # Run the learning experiment for a defined number of epochs (iterations).
    for epoch in range(epochs):
        # Set the initial loss/error and the number of accurate predictions to zero.
        training_loss = 0.0
        training_accurate_predictions = 0

        for i in range(len(training_images)):
            # Forward propagation/forward pass:
            # 1. The input layer: Initialize the training image data as inputs.
            layer_0 = training_images[i]
            # 2. The hidden layer:
            #    Take in the training image data into the middle layer by
            #    matrix-multiplying it by randomly initialized weights.
            layer_1 = numpy.dot(layer_0, weights_1)
            # 3. Pass the hidden layer's output through the ReLU activation function.
            layer_1 = relu(layer_1)
            # 4. Define the dropout function for regularization.
            dropout_mask = rng.integers(low=0, high=2, size=layer_1.shape)
            # 5. Apply dropout to the hidden layer's output.
            layer_1 *= dropout_mask * 2
            # 6. The output layer:
            #    Ingest the output of the middle layer into the final layer
            #    by matrix-multiplying it by randomly initialized weights.
            layer_2 = numpy.dot(layer_1, weights_2)

            # Backpropagation/backward pass:
            # 1. Measure the training error (loss function) between the actual
            #    image labels (the truth) and the prediction by the model.
            training_loss += numpy.sum((training_labels[i] - layer_2) ** 2)
            # 2. Increment the accurate prediction count.
            training_accurate_predictions += int(
                numpy.argmax(layer_2) == numpy.argmax(training_labels[i]))
            # 3. Differentiate the loss function/error.
            layer_2_delta = training_labels[i] - layer_2
            # 4. Propagate the gradients of the loss function back through the hidden layer.
            layer_1_delta = numpy.dot(weights_2, layer_2_delta) * relu2deriv(layer_1)
            # 5. Apply the dropout to the gradients.
            layer_1_delta *= dropout_mask
            # 6. Update the weights for the middle and input layers
            #    by multiplying them by the learning rate and the gradients.
            weights_1 += learning_rate * numpy.outer(layer_0, layer_1_delta)
            weights_2 += learning_rate * numpy.outer(layer_1, layer_2_delta)
        
        # Store training set losses and accurate predictions.
        store_training_loss.append(training_loss)
        store_training_accurate_pred.append(training_accurate_predictions)

        # Evaluate model performance on the test set at each epoch.
        #
        # Unlike the training step, the weights are not modified for each image
        # (or batch). Therefore the model can be applied to the test images in a
        # vectorized manner, eliminating the need to loop over each image
        # individually.

        results = relu(test_images @ weights_1) @ weights_2

        # Measure the error between the actual label (truth) and prediction values.
        test_loss = numpy.sum((test_labels - results) ** 2)

        # Measure prediction accurracy on test set.
        test_accurate_predictions = numpy.sum(
            numpy.argmax(results, axis=1) == numpy.argmax(test_labels, axis=1))
        
        # Store test set losses and accurate predictions.
        store_test_loss.append(test_loss)
        store_test_accurate_pred.append(test_accurate_predictions)

        print((
            f"Epoch: {epoch}\n"
            f"  Training set error: {training_loss / len(training_images):.3f}\n"
            f"  Training set accuracy: {training_accurate_predictions / len(training_images)}\n"
            f"  Test set error: {test_loss / len(test_images):.3f}\n"
            f"  Test set accuracy: {test_accurate_predictions / len(test_images)}"
        ))
