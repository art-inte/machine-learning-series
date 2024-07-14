def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)

if __name__ == '__main__':
    ask_ok('Do you really want to quit? ')
    ask_ok('OK to overwrite the file?' , 2)
    ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no!')

