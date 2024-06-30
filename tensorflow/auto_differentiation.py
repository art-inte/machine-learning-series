import numpy
import tensorflow

if __name__ == '__main__':
    x = tensorflow.Variable(3.0)
    with tensorflow.GradientTape() as tape:
       y = x**2    
    # dy = 2x * dx
    dy_dx = tape.gradient(y, x)
    print(dy_dx.numpy())