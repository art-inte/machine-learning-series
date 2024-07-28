import keras
import numpy

class MyDense(keras.layers.Layer):
    def __init__(self, units, activation=None, name=None):
        super().__init__(name=name)
        self.units = units
        self.activation = keras.activations.get(activation)
    
    def build(self, input_shape):
        input_dim = input_shape[-1]
        self.w = self.add_weight(
            shape=(input_dim, self.units),
            initializer=keras.initializers.GlorotNormal(),
            name='kernel',
            trainable=True)
        self.b = self.add_weight(
            shape=(self.units,),
            initializer=keras.initializers.Zeros(),
            name='bias',
            trainable=True)

    def call(self, inputs):
        # Use keras ops to create backend-agnostic layer/metrics/etc.
        x = keras.ops.matmul(inputs, self.w) + self.b
        return self.activation(x)

class MyDropout(keras.layers.Layer):
    def __init__(self, rate, name=None):
        super().__init__(name=name)
        self.rate = rate
        # Use seed_generator for managing RNG state.
        # It is a state element and its seed variable is
        # tracked as part of layer.variables.
        self.seed_generator = keras.random.SeedGenerator(1337)

    def call(self, inputs):
        return keras.random.dropout(inputs, self.rate, seed=self.seed_generator)
    
class MyModel(keras.Model):
    def __init__(self, num_classes):
        super().__init__()
        self.conv_base = keras.Sequential([
            keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
            keras.layers.GlobalAveragePooling2D(),]
        )
        self.dropout = MyDropout(0.5)
        self.dense = MyDense(num_classes, activation='softmax')
    
    def call(self, x):
        x = self.conv_base(x)
        x = self.dropout(x)
        return self.dense(x)

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    # Scale images to the [0, 1] range.
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    # Make sure images have shape (28, 28, 1).
    x_train = numpy.expand_dims(x_train, -1)
    x_test = numpy.expand_dims(x_test, -1)

    model = MyModel(num_classes=10)
    
    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(),
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        metrics=[
            keras.metrics.SparseCategoricalAccuracy(name='acc'),
        ],
    )

    batch_size = 128
    epochs = 20
    model.fit(
        x_train,
        y_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.15,
    )
    score = model.evaluate(x_test, y_test, verbose=0)
    predictions = model.predict(x_test)
    print(predictions[0])
