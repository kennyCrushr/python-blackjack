import random

game_active = True # Declaring this for the game loop later
cash = 0
consistent_wins = 0
MAX_WIN_LIMIT = 5

print("Welcome to Kenny's Casino")
print("How much are we betting today?")
betting_cash = int(input("Place the amount of cash: "))

if betting_cash <= 0:
  print("Let's give you some cash.")
  betting_cash = 1000

