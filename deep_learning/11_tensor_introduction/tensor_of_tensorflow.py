import matplotlib.pyplot as pyplot
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
    rank_3_tensor = tf.constant([
        [[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]],
        [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],
        [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]],
    ])

    ax = pyplot.axes(projection='3d')
    for i in range(rank_3_tensor.shape[0]):
        for j in range(rank_3_tensor.shape[1]):
            for k in range(rank_3_tensor.shape[2]):
                ax.scatter3D(i, j, k)
    pyplot.show()
