#!/usr/bin/env python

stack = []


def pushit():
    stack.append(input('Enter new string: '))


def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack!')
    else:
        print('Removed [', stack.pop(), ']')


def viewstack():
    print(str(stack))


def show_menu():
    prompt = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter choice:
    """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt) as err:
                print("err")
                choice = 'q'
            print('\nYou picked:[%s]' % choice)
            if choice not in 'uovq':
                print('invalid option, try again', end='')
            else:
                chosen = True
        if choice == 'q': done = 1
        if choice == 'u': pushit()
        if choice == 'o': popit()
        if choice == 'v': viewstack()


if __name__ == '__main__':
    show_menu()
