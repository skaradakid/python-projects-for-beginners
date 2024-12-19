from random import choice

def roll():
    lst = [1,2,3,4,5,6]
    print((choice(lst),choice(lst)))

while True:
    inpt = input('Roll dice y/n> ')
    if inpt == 'n':
        print('Thank you for playing')
        exit()
    elif inpt == 'y':
        roll()
    else:
        print('Invalid choice!')
