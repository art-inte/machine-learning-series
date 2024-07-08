import numpy

if __name__ == '__main__':
    a = numpy.arange(10)
    print('Third element:', a[2])
    print('Second element from the last:', a[-2])

    a.shape = (2, 5) # now x is 2-dimensional
    print(a[1, 3], a[1][3], a[1, -3], a[1][-3])
 
    print(a[1])

    b = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(b[1:7:2])

