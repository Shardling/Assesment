#imports all the modules I will use
import os
import random
import time
from simple_chalk import chalk
#lists for chalks, questions, and answers.
CHALKS = ["seahorse", "Genie's Dogfish", "plankton", "shrimp", "octopus", "starfish", "Russia", "Winston Churchill", "Cretaceous", "Julius Caesar", "Germany"]
A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} period end?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
A1 = ["fish", "shark", "whale", "9", "no", "ww1", "ww2", "65000000", "23", "No"]
#lists for user inputs, scores, scorekeeping, and how many times the sub-function has run.
Ui = []
counter = 0
yes = 0
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#defines a sub program for updating t_score if i want to.
def score_check():
  #global allows you to use variables outside the sub-function.
  global t_score
  #adds all the scores together.
  t_score = scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5] + scores[6] + scores[7] + scores[8] + scores[9]
#defines sub-function to choose a random question.
def randques():
  global t, func, up
  #chooses random question from list.
  func = random.choice(A_1)
  #if the value pulled is 0, it will try again. this will be explaied later.
  while func == 0:
    func = random.choice(A_1)
  #think of t as a number corresponding to the question and pulls it as its corresponding question is pulled randomly
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
  #prints the question.
  print(func)
#another sub program. this is the skeleton which will be used instead of using it 10 times for different questions.
def Q():
  #uses randques to pull a random question.
  randques()
  global counter, scores, yes
  #while loop allows the repeat of the question if they get it incorrect.
  while True:
    #calls for a user input.
    Q = input("")
    #if the user hasn't already typed this during this question, then...
    if Q not in Ui:
      #checks if it is the correct answer.
      if Q.lower() == A1[t].lower():
        #changes variables so the programe can tell the user completed a question.
        print("Congrats you are correct!")
        yes = yes + 1
        #adds count to the counter so a score can be added
        counter = counter + 1
        #score in spot t is now equal to the counter
        scores[t] = counter
        #resets the counter
        counter = 0
        time.sleep(2)
        #clears the console
        os.system('clear')
        #clears the guess list.
        Ui.clear()
        #changes the question to 0 so it cant be used again(as explained in randques function)
        A_1[t] = 0
        return
      #if users guess is incorrect
      else:
        counter = counter + 1
        #adds users guess to a list.
        Ui.append(Q)
        print("Incorrect.")
        time.sleep(2)
        os.system('clear')
    #if the user has already tried this guess before
    else:
      print("""You have already tried this.
It will therefore not be added to your score""")
      time.sleep(2)
      os.system('clear')
#prints the rules i guess
print("The lower your score, the better you performed.")
#while yes is less than 10 it will repeat this. this means the sub-function will be used 10 times.
while yes < 10:
  Q()
#checks score and prints it.
score_check()
print("your score is:", t_score)
