import tensorflow

if __name__ == '__main__':
    # This will be an int32 tensor by default; see 'dtypes' below.
    rank_0_tensor = tensorflow.constant(4)
    print(rank_0_tensor)
