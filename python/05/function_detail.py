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

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print("-- It's", state, '!')

if __name__ == '__main__':
    ask_ok('Do you really want to quit? ')
    ask_ok('OK to overwrite the file?' , 2)
    ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no!')

    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action='VOOOOOM')
    parrot(action='VOOOOOM', voltage=1000000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')

