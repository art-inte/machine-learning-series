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

    # for statement
    # measure some strings
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

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
        print(i, a[i])

    print(range(10))
