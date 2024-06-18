import keras
import tensorflow as tf
import tensorflow_datasets

epochs = 5
batch_size = 32

loss_fn = keras.losses.SparseCategoricalCrossentropy()
optimizer = keras.optimizers.Adam()

train_loss = keras.metrics.Mean(name='train_loss')
train_accuracy = keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

@tf.function
def train_step(model, images, labels):
    with tf.GradientTape() as tape:
        # training=True is only need if there are layers with different
        # behavior during training versus inference (e.g. Dropout).
        predictions = model(images)
        loss = loss_fn(label, predictions)

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    # train_loss(loss)
    # train_accuracy(labels, predictions)


class MnistModel(keras.Model):
    def __init__(self):
        super().__init__()
        self.flatten = keras.layers.Flatten()
        self.d1 = keras.layers.Dense(128, activation='relu')
        self.d2 = keras.layers.Dense(10, activation='softmax')
    
    def call(self, x):
        x = self.flatten(x)
        x = self.d1(x)
        return self.d2(x)


if __name__ == '__main__':
    print('TensorFlow version: ', tf.__version__)

    (x_train, y_train), (x_test, y_test) = tensorflow_datasets.as_numpy(
        tensorflow_datasets.load(
        'mnist',
        split=['train', 'test'],
        batch_size=-1,
        as_supervised=True,
    ))
    x_train, x_test = x_train / 255.0, x_test / 255.0
    print('Shape of train image:', x_train.shape)
    print('Shape of test image:', x_test.shape)
    
    # Create an instance of the model.
    mnist_model = MnistModel()

    for epoch in range(epochs):
        train_loss.reset_state()
        train_accuracy.reset_state()

        for image, label in zip(x_train, x_test):
            train_step(mnist_model, image, label)

        print(
            f'Epoch {epoch + 1}, '
            f'Loss: {train_loss.result():0.2f}, '
            f'Accuracy: {train_accuracy.result() * 100:0.2f}')