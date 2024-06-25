if __name__ == '__main__':
    print("Hello, world!")
    print('Got your back')
    # use \' to escape the single quote
    print('doesn\'t')
    print("doesn't")
    print('First line.\nSecond line.')
    print(r'C:\some\name')

    word = 'Python'
    print(word[0])
    print(word[5])

    # Fibonacci series:
    # the sum of two elements defines the next
    a, b = 0, 1
    while a < 10:
        print(a, end=' ')
        a, b = b, a + b
    print()
