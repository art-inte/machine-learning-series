import numpy

def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    z = 0
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z

def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]
    z = numpy.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z

def naive_matrix_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]
    z = numpy.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)
    return z

if __name__ == '__main__':
    a = numpy.array([1, 2, 3, 4, 5])
    b = numpy.array([1, 2, 3, 4, 5])
    assert naive_vector_dot(a, b) == (1 + 4 + 9 + 16 + 25)

    c = numpy.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15]])
    
    d = numpy.transpose(c)
    
    assert (naive_matrix_vector_dot(c, b) == c.dot(b)).all()
    assert ((naive_matrix_dot(c, d)) == c.dot(d)).all()
