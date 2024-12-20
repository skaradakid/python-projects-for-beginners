import random

cpu_choices = ['Rock', 'Paper', 'Scissors']
game = [{('rock', 'paper'): 'paper'}, {('rock', 'scissors'): "rock"}, {('scissors', 'paper'): 'scissors'}]

while True:

    player_choice = input("Rock , Paper or Scissors (r,p,s): ")
    if player_choice == "r":
        player_choice = "Rock"
    elif player_choice == "p":
        player_choice = 'Paper'
    elif player_choice == "s":
        player_choice = "Scissors"
    cpu_choice = random.choice(cpu_choices)
    
    if player_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid!") 
    else:
        print(f'you chose {player_choice}')
        print(f"cpu chose {cpu_choice}")
        
        while True:
          end_game = input('want to continue?: ')
          
          if end_game == 'n':
              print('Thank you for playing')
              exit()
          elif end_game == "y":
              break
          else: 
              print("Invalid!")