import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Set up a list for player input reference
player_options = [rock, paper, scissors]
computer_input = random.choice(player_options)
computer_index = player_options.index(computer_input)

player_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

#Player Choice
if player_input >=3 or player_input < 0:
    print('That is not valid option. You lose')
elif player_input <=2 and player_input >=0:
    print(player_options[player_input])

#Computer Choice
print('Computer Chose')
print(computer_input)

#Logic to determine win/lose/draw
if player_input == computer_index:
    print('You have drawn')
elif ((player_input == 0 and computer_index == 1)
      or (player_input == 1 and computer_index == 2)
      or (player_input == 2 and computer_index == 0)):
    print('You lose')
elif ((player_input == 0 and computer_index == 2)
      or (player_input == 2 and computer_index == 1)
      or (player_input == 1 and computer_index == 0)):
    print('You win')