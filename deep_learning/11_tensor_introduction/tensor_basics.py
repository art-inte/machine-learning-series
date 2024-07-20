import numpy
import tensorflow


if __name__ == '__main__':
    # This will be an int32 tensor by default; see 'dtype' below.
    rank_0_tensor = tensorflow.constant(4)
    print(rank_0_tensor)
    # Let's make this a float tensor.
    rank_1_tensor = tensorflow.constant([2.0, 3.0, 4.0])
    print(rank_1_tensor)
    # If you want to be specific, you can set the dtype (see below) at creation time.
    rank_2_tensor = tensorflow.constant([[1, 2], [3, 4], [5, 6]], dtype=tensorflow.float16)
    print(rank_2_tensor)

    # There can be an arbitrary number of
    # axes (sometimes called "dimensions")
    rank_3_tensor = tensorflow.constant([
        [[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]],
        [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],
        [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]],
    ])

    print(numpy.array(rank_2_tensor))
    print(rank_2_tensor.numpy())

    a = tensorflow.constant([[1, 2], [3, 4]])
    b = tensorflow.constant([[1, 1], [1, 1]])
    print(tensorflow.add(a, b))
    print(tensorflow.multiply(a, b))
    print(tensorflow.matmul(a, b))

    print(a + b)
    print(a * b)
    print(a @ b)

    c = tensorflow.constant([[4.0, 5.0], [10.0, 1.0]])
    # Find the largest value.
    print(tensorflow.reduce_max(c))
    # Find the index of the largest value.
    print(tensorflow.math.argmax(c))
    # Compute the softmax
    print(tensorflow.nn.softmax(c))

    tensorflow.convert_to_tensor([1, 2, 3])
    tensorflow.reduce_max([1, 2, 3])
    tensorflow.reduce_max(numpy.array([1, 2, 3]))  
