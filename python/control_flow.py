if __name__ == '__main__':
    # if statement
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

    # measure some strings
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print('Word', w, 'len is', len(w))

    # create a sample collection
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    print(active_users)

    # range function
    for i in range(5):
        print(i, end=' ')
    print()

    print(list(range(0, 10, 3)))

    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        if i < len(a) - 1:
            print(i, a[i], end=', ')
        else:
            print(i, a[i])

    for i in range(10):
        if i == 5:
            break
        print(i, end=' ')
    print()

    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print()

    status = int(input("Please enter a http error: "))
    match status:
        case 400:
            print('Bad request')
        case 404:
            print('Not found')
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")
