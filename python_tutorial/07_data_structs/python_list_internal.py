
if __name__ == '__main__':
    str_list = [
        'The empty vessels make the greatest sound.',
        'The retention will never give up.',
        'To be or not to be. That is a question.',
        'A light heart lives long.',
        ' Nothing is so common as the wish to be remarkable.'
    ]

    address0 = hex(id(str_list[0]))
    address1 = hex(id(str_list[1]))
    address2 = hex(id(str_list[2]))
    print(address0, address1, address2)
    

