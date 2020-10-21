import random

score_number = 0
counter_check = 0


name = input("Enter your name: ")
print(f"Hello, {name}")

    
game_types = input("Input which variables you would like to play with. Input nothing if you want to play the classic rock, paper, and scissors: ")

def game():
  global score_number
  choices = ["rock", "paper", "scissors"]
  selected_choice = random.choice(choices)

  inp = input("Okay, type in your choice or command: ")

  if inp == "!exit":
    print("Bye!")
    exit()

  elif inp == "!rating":
    print(f"Your rating: {score_number}")
    game()

  elif inp not in choices:
    print("Invalid input")
    game()

  elif inp == selected_choice:
    print(f"There is a draw ({selected_choice})")
    score_number += 50
    game()

  elif selected_choice == "rock" and inp == "paper":
    print("Well done. The computer chose rock and failed")
    score_number += 100
    game()

  elif selected_choice == "paper" and inp == "scissors":
    print("Well done. The computer chose paper and failed")
    score_number += 100
    game()

  elif selected_choice == "scissors" and inp == "rock":
    print("Well done. The computer chose scissors and failed")
    score_number += 100
    game()

  elif selected_choice == "rock" and inp == "scissors":
    print("Sorry, but the computer chose rock")
    game()

  elif selected_choice == "paper" and inp == "rock":
    print("Sorry, but the computer chose paper")
    game()

  elif selected_choice == "scissors" and inp == "paper":
    print("Sorry, but the computer chose scissors")
    game()

def extended():
  global score_number
  global counter_check
  global game_types


  items = list(game_types.split(","))
  new_selected = random.choice(items)
  # middle = int(len(items) / 2)

  inp = input("Okay, type in your choice or command: ")


  if inp == "!exit":
    print("Bye!")
    exit()

  elif inp == "!rating":
    print(f"Your rating: {score_number}")
    extended()
  
  else:
    winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


    if inp == new_selected:
      score_number += 50
      print(f"There is a draw ({new_selected})")
      extended()
    
    elif inp not in items:
      print("Invalid input")
      extended()
    
    
    elif inp != new_selected and new_selected in winning_cases.keys():
      for key in winning_cases.keys():
        if inp == key:
          if new_selected in winning_cases[key]:
            score_number += 100
            print(f"Well done. The computer chose {new_selected} and failed")
            extended()
          elif new_selected not in winning_cases[key]:
            print(f"Sorry, but the computer chose {new_selected}")
            extended()
            break




if game_types == "":
  print("Okay, let's start")
  game()

else:
  print("Okay, let's start")
  extended()
