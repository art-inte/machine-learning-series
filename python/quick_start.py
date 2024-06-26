if __name__ == '__main__':
    print("Hello, world!")
    print('Got your back')
    # use \' to escape the single quote
    print('doesn\'t')
    print("doesn't")
    print('First line.\nSecond line.')
    print(r'C:\some\name')

    print(3 * 'un' + 'ium')
    print('Py' 'thon')
    text = ('Put several strings within parentheses '
            'to have them joined together.')
    print(text)

    word = 'Python'
    print(word[0])
    print(word[5])
    print(word[-1])
    print(word[-2])
    print(word[-6])
    print(word[0:2])    # characters from the beginning to position 2 (excluded)
    print(word[2:5])    # characters from position 2 (included) to 5 (excluded)
    print(word[:2])     # characters from the beginning to position 2 (excluded)
    print(word[4:])     # characters from position 4 (included) to the end
    print(word[-2:])    # characters from the second-last (included) to the end
    print(word[:2] + word[2:])
    print(word[:4] + word[4:])
    print(word[4:42])
    print('J' + word[1:])
    print(word[:2] + 'py')

    squares = [1, 4, 9, 16, 25]
    print(squares)
    print(squares[0])   # indexing returns a value
    print(squares[-1])
    print(squares[-3:]) # slicing returns a new list
    print(squares + [36, 49, 64, 81, 100])

    cubes = [1, 8, 27, 65, 125]
    print(cubes)
    cubes[3] = 64   # replace the wrong value
    print(cubes)

    cubes.append(216)   # add the cube of 6
    cubes.append(7 ** 3)    # and the cube of 7
    print(cubes)

    rgb = ['Red', 'Green', 'Blue']
    rgba = rgb
    print(id(rgb) == id(rgba))
    rgba.append('Alph')
    print(rgb)

    correct_rgba = rgba[:]
    correct_rgba[-1] = 'Alpha'
    print(correct_rgba)
    print(rgba)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    print(letters)
    letters[2:5] = []  # remove some values
    print(letters)
    letters[:] = []  # clear the list by replacing all the elements with an empty list
    print(letters)

    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    nest_list = [a, b]
    print(nest_list)
    print(nest_list[0])
    print(nest_list[0][1])

    # Fibonacci series:
    # the sum of two elements defines the next
    a, b = 0, 1
    while a < 10:
        print(a, end=' ')
        a, b = b, a + b
    print()
