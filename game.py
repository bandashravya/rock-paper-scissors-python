#stone paper scissor game
import random
choices=['stone','paper','scissor']


while True:
  player = input("enter your choice(stone'/paper'/scissor): ")
  computer=random.choice(choices)
  print("computer choice: ",computer)
  print("player choice: ",player)
  if(player==computer):
    print("draw")
  elif (player == 'stone' and computer == 'scissor') or \
     (player == 'paper' and computer == 'stone') or \
     (player == 'scissor' and computer == 'paper'):
     print("player wins")
  else:
       print("computer wins")
  again=input("play again?(yes/no)")
  if (again=="yes"):
     continue
  else:
     break