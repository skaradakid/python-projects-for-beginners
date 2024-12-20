import random

while True:
    choice = input("Rock , Paper or Scissors (r,p,s): ")
    if choice not in "rps":
        print("Invalid!") 
    else:
        print('valid!')
        while True:
          end_game = input('want to continue?: ')
          if end_game == 'n':
              print('Thank you for playing')
              exit()
          elif end_game == "y":
              break
          else: 
              print("Invalid!")