#importing objects to use for clearing console.
import os
import time
import random
from simple_chalk import chalk
#make the lists for the answers and the user inputted answers.
A1 = ["fish", "shark", "whale", "9", "no"]
A2 = ["ww2", "ww1", "65000000", "23", "No"]
Ui = []
#Variables
counter = 0
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
CHALKS = ["seahorse", "Genie's Dogfish", "plankton", "shrimp", "octopus", "starfish", "Sea Creatures", "History", "Russia", "Winston Churchill", "Cretaceous", "Julius Caesar", "Germany"]
#Sub programs
def Theme():
  #this makes any variables defined here able to be used anywhere
  global M1
  print("please choose a theme: ")
  print(chalk.blue(CHALKS[6]))
  print(chalk.red(CHALKS[7]))
  M1 = input("")
def randfunc():
  func = random.choice(func_list)
  func_use = func()
  print(func_use)
  score_check()
  os.system('clear')
  print("Your score is: ", t_score)
  time.sleep(2)
  os.system('clear')
  func_list.remove(func)
def randfunc_2():
  func = random.choice(func_list_2)
  func_use = func()
  print(func_use)
  score_check()
  os.system('clear')
  print("Your score is: ", t_score)
  time.sleep(2)
  os.system('clear')
  func_list_2.remove(func)
#each time this is used it defines a variable as everything there added together. 
def score_check():
  global t_score
  #adds all the scores together to make a total.
  t_score = scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5] + scores[6] + scores[7] + scores[8] + scores[9]
#sub programs for 'sea creatures topic'
def Q1_S():
  global counter, score
  #while loop to keep the user looping until correct answer is found
  while True:
    print(f"What species is a {chalk.blue(CHALKS[0])}?")
    Q1 = input("")
    #checks if the answer the user gave has been inputted before
    if Q1 not in Ui:
      #checks if answer is correct
      if Q1.lower() == A1[0].lower():
        print("Congrats,", chalk.green(Q1), "is correct!")
        #this boosts the counter and then assigns it to a score variable and then is reset
        counter = counter + 1
        scores[0] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        #adds to counter and adds input to list
        counter = counter + 1
        Ui.append(Q1)
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q2_S():
  global counter, score_2
  while True:
    print(f"What species is a {chalk.blue(CHALKS[1])}")
    Q2 = input("")
    if Q2 not in Ui:
      if Q2.lower() == A1[1].lower():
        print("Congrats,", chalk.green(Q2), "is correct!")
        counter = counter + 1
        scores[1] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q3_S():
  global counter, score_3
  while True:
    print(f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?")
    Q3 = input("")
    if Q3 not in Ui:
      if Q3.lower() == A1[2].lower():
        print("Congrats,", chalk.blue(Q3), "is correct!")
        counter = counter + 1
        scores[2] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q3)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q4_S():
  global counter, score_4
  while True:
    print(f"How many brains does an {chalk.blue(CHALKS[4])} have?")
    Q4 = input("")
    if Q4 not in Ui:
      if Q4.lower() == A1[3].lower():
        print("Congrats,", chalk.green(Q4), "is correct!")
        counter = counter + 1
        scores[3] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q4)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q5_S():
  global counter, score_5
  while True:
    print(f"Is a {chalk.blue(CHALKS[5])} a fish?")
    Q5 = input("")
    if Q5 not in Ui:
      if Q5.lower() == A1[4].lower():
        print("Congrats,", chalk.green(Q5), "is correct!")
        counter = counter + 1
        scores[4] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q5)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
#using all the sub programs to make a complete quiz

def Q1_H():
  global counter, score
  #while loop to keep the user looping until correct answer is found
  while True:
    print(f"in what war did {chalk.red(CHALKS[8])} pull out of?")
    Q1_2 = input("")
    #checks if the answer the user gave has been inputted before
    if Q1_2 not in Ui:
      #checks if answer is correct
      if Q1_2.lower() == A2[1].lower():
        print("Congrats,", chalk.green(Q1_2), "is correct!")
        #this boosts the counter and then assigns it to a score variable and then is reset
        counter = counter + 1
        scores[5] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        #adds to counter and adds input to list
        counter = counter + 1
        Ui.append(Q1_2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q2_H():
  global counter, score_2
  while True:
    print(f"In what war was {chalk.red(CHALKS[9])} in office?")
    Q2_2 = input("")
    if Q2_2 not in Ui:
      if Q2_2.lower() == A2[0].lower():
        print("Congrats,", chalk.green(Q2_2), "is correct!")
        counter = counter + 1
        scores[6] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q2_2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q3_H():
  global counter, score_3
  while True:
    print(f"How many years ago did the {chalk.red(CHALKS[10])} period end?")
    Q3_2 = input("")
    if Q3_2 not in Ui:
      if Q3_2.lower() == A2[2].lower():
        print("Congrats,", chalk.blue(Q3_2), "is correct!")
        counter = counter + 1
        scores[7] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        return
      else:
        counter = counter + 1
        Ui.append(Q3_2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q4_H():
  global counter, score_4
  while True:
    print(f"How many times did {chalk.red(CHALKS[11])} get stabbed?")
    Q4_2 = input("")
    if Q4_2 not in Ui:
      if Q4_2.lower() == A2[3].lower():
        print("Congrats,", chalk.green(Q4_2), "is correct!")
        counter = counter + 1
        scores[8] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q4_2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
def Q5_H():
  global counter, score_5
  while True:
    print(f"did {chalk.red(CHALKS[12])} start ww1?")
    Q5_2 = input("")
    if Q5_2 not in Ui:
      if Q5_2.lower() == A2[4].lower():
        print("Congrats,", chalk.green(Q5_2), "is correct!")
        counter = counter + 1
        scores[9] = counter
        counter = 0
        time.sleep(1.5)
        os.system('clear')
        Ui.clear()
        return
      else:
        counter = counter + 1
        Ui.append(Q5_2)
        print("Incorrect.")
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
#using all the sub programs to make a complete quiz

func_list = [Q1_S, Q2_S, Q3_S, Q4_S, Q5_S]
func_list_2 = [Q1_H, Q2_H, Q3_H, Q4_H, Q5_H]
while len(func_list):
  Theme()
  if M1.lower() == "sea creatures":
    print("Remember, the lower the score, the better you did!")
    #uses the sub programs and then checks score and clears the console and gives you your score. repeat.
    while len(func_list):
      randfunc()
    print("Do you want to try again?")
    ans = input("")
    if ans.lower == "yes":
      print("Please continue")
      os.system('clear')
    else:
      break
  elif M1.lower() == "history":
    print("Remember, the lower the score, the better you did!")
    while len(func_list_2):
      randfunc_2()
    print("Do you want to try again?")
    ans = input("")
    if ans.lower == "yes":
      print("Please continue")
      os.system('clear')
  else:
    os.system('clear')
if t_score >= 10:
  print("Congrats! With this minigame, you can lower your score!")
