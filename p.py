#imports modules and libraries
import random
import time
import os
import chalk
#makes variables for chalk and the scoring system and gives the user
CHALKS_3 = ["lower", "unexpected", 12, "High", "Low"]
scored = 12
print(f"Would you like a chance to {chalk.cyan(CHALKS_3[0])} your score via other means?")
print("Even if you replay, you cannot change this score.")
score_lower = input("")
time.sleep(2)
os.system('clear')
#if user answert is yes, it starts the game
if score_lower.lower() == "yes":
  print("""Guess a number between 1 and 50. The program will tell
you if your guess is too high or too low. You have 12 tries.
whatever is left once you have guessed the number will be deducted
from your score!

Good Luck.""")
  time.sleep(6)
  os.system('clear')
  #generates random number and initiates a loop
  RNG = random.randint(1, 50)
  while scored > 0:
    #tells user the number of guesses remaining and asks for an input
    print("You have", chalk.blue(scored), "guesses left.")
    time.sleep(1)
    ans = input("")
    ans_list = ans.rsplit(".")
    #try and except to catch a value error while looking for a float or integer.
    try:
      #if all of these exist and are integers, it becomes a float
      ans_1 = ans_list[0]
      ans_2 = ans_list[1]
      ans = float(ans_1 + "." + ans_2)
    except(IndexError, TypeError, ValueError):
      if ans_1.isdigit() == True:
        ans = float(ans_list[0])
      else:
        scored = scored - 12
        print(f"You inputted an {chalk.red(CHALKS_3[1])} value, this has a {chalk.cyan(CHALKS_3[2])} guess penalty.")
        time.sleep(2)
        os.system('clear')
        break
    if ans == RNG:
      scored = scored - 1
      print("Correct!,", chalk.cyan(scored), "points will be deducted from your score")
      time.sleep(1)
      os.system('clear')
      break
    elif ans > RNG:
      scored = scored - 1
      print("Your guess is too", chalk.red(CHALKS_3[3]))
      time.sleep(1)
      os.system('clear')
    elif ans < RNG:
      scored = scored - 1
      print("Your guess is too", chalk.red(CHALKS_3[4]))
      time.sleep(1)
      os.system('clear')
else:
  scored = 0
