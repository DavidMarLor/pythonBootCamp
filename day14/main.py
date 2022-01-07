from art import logo
from game_data import data

print(logo)

import random 

game = 'true'
score = 0

while game == 'true':
  first_pick = random.choice(data)
  second_pick = random.choice(data)

  print(first_pick['name'] + ' vs ' + second_pick['name'])
  selection = input("Type your selection: ")
  if first_pick['follower_count'] > second_pick['follower_count']:
    winner = first_pick['name']
  else:
    winner = second_pick['name']

  if selection.lower() == winner.lower():
    print("You're right!!")
    score+=1
  else:
    print("You're wrong!!")
    game = 'false'

print(score)

