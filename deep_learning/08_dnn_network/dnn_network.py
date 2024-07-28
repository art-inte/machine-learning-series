import keras
import matplotlib.pyplot as pyplot
# pip install scikit-learn
from sklearn.datasets import make_moons

if __name__ == '__main__':
    x, y = make_moons(n_samples=100, noise=0.1)
    y = y * 2 - 1
    # visualize in 2D
    pyplot.figure(figsize=(5, 5))
    pyplot.scatter(x[:, 0], x[:, 1], c=y, s=20, cmap='jet')
    pyplot.subplots_adjust(left=0.1, right=0.9, top=0.96, bottom=0.06)
    pyplot.savefig('temp/make_moons.png', dpi=300)
    pyplot.show()

    model = keras.Sequential([
        keras.layers.Input(shape=(2,)),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(1)
    ])
    model.summary()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x, y, epochs=10, batch_size=8, verbose=2)
