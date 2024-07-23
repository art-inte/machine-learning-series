import keras
import tensorflow

if __name__ == '__main__':
    x = tensorflow.Variable(3.0)
    with tensorflow.GradientTape() as tape:
        y = x**2
    # dy = 2x * dx
    dy_dx = tape.gradient(y, x)
    print('The gradient of dy/dx', dy_dx.numpy())

    w = tensorflow.Variable(tensorflow.random.normal((3, 2)), name='w')
    b = tensorflow.Variable(tensorflow.zeros(2, dtype=tensorflow.float32), name='b')
    x = [[1.0, 2.0, 3.0]]
    with tensorflow.GradientTape(persistent=True) as tape:
        # shape(1, 2) = shape(1, 3) * shape(3, 2)
        y = x @ w + b
        loss = tensorflow.reduce_mean(y**2)    
    [dl_dw, dl_db] = tape.gradient(loss, [w, b])
    print('The gradient of dl/dw', dl_dw)
    print('The gradient of dl/db', dl_db)

    print('Shape of w', w.shape)
    print('Shape of gradient dl/dw', dl_dw.shape)
    vars_dict = { 'w': w, 'b': b}
    grad = tape.gradient(loss, vars_dict)
    print(grad['w'])
    print(grad['b'])

    layer = keras.layers.Dense(2, activation='relu')
    x = tensorflow.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    with tensorflow.GradientTape() as tape:
        # forward pass
        y = layer(x)
        loss = tensorflow.reduce_mean(y**2)
    # Calculate gradients with respect to every trainable variable
    grad = tape.gradient(loss, layer.trainable_variables)
    for var, g in zip(layer.trainable_variables, grad):
        print(f'{var.name}, shape: {g.shape}')
