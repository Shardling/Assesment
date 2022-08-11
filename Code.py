import os
import random
import time
from simple_chalk import chalk

CHALKS = ["seahorse", "Genie's Dogfish", "plankton", "shrimp", "octopus", "starfish", "Russia", "Winston Churchill", "Cretaceous", "Julius Caesar", "Germany"]
A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} period end?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
A1 = ["fish", "shark", "whale", "9", "no", "ww1", "ww2", "65000000", "23", "No"]
Ui = []
counter = 0
yes = 0
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def score_check():
  global t_score
  t_score = scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5] + scores[6] + scores[7] + scores[8] + scores[9]
def randfunc():
  global t, func, up
  func = random.choice(A_1)
  while func == 0:
    func = random.choice(A_1)
  if func == A_1[0]:
    t = 0
  elif func == A_1[1]:
    t = 1
  elif func == A_1[2]:
    t = 2
  elif func == A_1[3]:
    t = 3
  elif func == A_1[4]:
    t = 4
  elif func == A_1[5]:
    t = 5
  elif func == A_1[6]:
    t = 6
  elif func == A_1[7]:
    t = 7
  elif func == A_1[8]:
    t = 8
  elif func == A_1[9]:
    t = 9
  print(func)
def Q():
  randfunc()
  global counter, scores, yes
  while True:
    Q5 = input("")
    if Q5 not in Ui:
      if Q5.lower() == A1[t].lower():
        print("Congrats you are correct!")
        yes = yes + 1
        counter = counter + 1
        scores[t] = counter
        counter = 0
        time.sleep(2)
        os.system('clear')
        score_check()
        print("your score is:", t_score)
        time.sleep(2)
        Ui.clear()
        A_1[t] = 0
        return
      else:
        counter = counter + 1
        Ui.append(Q5)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")

while yes < 10:
  Q()
