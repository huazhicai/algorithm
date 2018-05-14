#!/usr/bin/env python

# create our data structure
queue = []


# enQ() -- add string to end of queue
def enQ():
    queue.append(input('Enter new queue element: '))


# deQ() -- remove string from front of queue
def deQ():
    if len(queue) == 0:
        print('Cannot dequeue from empty queue!')
    else:
        print('Remove [', queue.pop(0), ']')


# viewQ() -- display queue contents
def viewQ():
    print(str(queue))


def show_menu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """

    # loop until user quits
    done = False
    while not done:
        # loop until user choses valid option
        chosen = False
        while not chosen:
            # if user hits ^C or ^D (EOF),
            # pretend they typed 'q' to quit
            try:
                choice = input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt) as err:
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            # validate option chosen
            if choice not in 'devq':
                print('invalid option, try again')
            else:
                chosen = True

        # take appropriate action
        if choice == 'q':
            done = True
        elif choice == 'e':
            enQ()
        elif choice == 'd':
            deQ()
        elif choice == 'v':
            viewQ()


# run show_menu() as the application
if __name__ == '__main__':
    show_menu()
