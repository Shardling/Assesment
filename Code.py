#imports all the modules I will use
import os
import random
import time
from simple_chalk import chalk
#lists for chalks, questions, and answers.
CHALKS = ["seahorse", "Genie's Dogfish", "plankton", "shrimp", "octopus", "starfish", "Russia", "Winston Churchill", "Dinosaurs", "Julius Caesar", "Germany"]
A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} go extinct?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
CHALKS_2 = ["HELL", "lower"]
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
    Q5 = input("")
    #if the user hasn't already typed this during this question, then...
    if Q5 not in Ui:
      #checks if it is the correct answer.
      if Q5.lower() == A1[t].lower():
        #changes variables so the programe can tell the user completed a question.
        print("Congrats, you are correct!")
        yes = yes + 1
        #adds count to the counter so a score can be added
        counter = counter + 1
        #score in spot t is now equal to the count
        scores[t] = counter
        counter = 0
        time.sleep(2)
        os.system('clear')
        Ui.clear()
        #clears A_1[t], so it wont be used again
        A_1[t] = 0
        return
      else:
        #if answer is incorrect, it tells you and adds to the count.
        counter = counter + 1
        Ui.append(Q5)
        print("Incorrect. If you tried an unabbreviated form of answer, please try it. E.G. ww2 instead of world war 2.")
        print("If that isnt the issue, if a number was asked of you, please use integers.")
        time.sleep(2)
    else:
      #if the user has tried this answer before it just resets the question
      print("""You have already tried this.
It will therefore not be added to your score""")
      time.sleep(2)

#Welcomes the user to the game
print(f"Welcome to {chalk.red(CHALKS_2[0])}, enjoy your stay.")
time.sleep(1)
#Explains the scoring system
print(f"The {chalk.cyan(CHALKS_2[1])} your score, the better you performed.")
#tells you the answers and gives you time to memorise them.
time.sleep(2)
os.system('clear')
print(chalk.blueBright(A1[0]))
time.sleep(0.2)
print(chalk.cyan(A1[1]))
time.sleep(0.2)
print(chalk.green(A1[2]))
time.sleep(0.2)
print(chalk.greenBright(A1[3]))
time.sleep(0.2)
print(chalk.yellowBright(A1[4]))
time.sleep(0.2)
print(chalk.redBright(A1[5]))
time.sleep(0.2)
print(chalk.red(A1[6]))
time.sleep(0.2)
print(chalk.magentaBright(A1[7]))
time.sleep(0.2)
print(chalk.magenta(A1[8]))
time.sleep(0.2)
print(chalk.blue(A1[9]))
time.sleep(0.2)
print("These are the answers, not in any particular order, so good luck!(You Have 15 seconds to memorise them)")
time.sleep(15)
os.system('clear')
#This loops it forever, or until a break command is used.
while True:
  #same as previous line, but for a smaller section of code
  while True:
    #This is the actual quiz, 2 lines, a loop, and using a function.
    while yes < 10:
      Q()
    #checks the score and prints it out, also asks user to play again for a lower score
    score_check()
    print("your score is:", t_score)
    print(f"Would you like to play again for a {chalk.cyan(CHALKS_2[1])} score?")
    replay = input("")
    #if user answer is yes, it resets everything, else, clears ui and breaks loop.
    if replay.lower() == "yes":
      A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} go extinct?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
      yes = 0
      scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
      time.sleep(3)
      os.system('clear')
      break
  #Uses p.py file, which is used for the higher-lower game
  import p
  #after p.py has run, it subtracts the score from the quiz score and tells the user their new score.
  if p.scored == 12:
    print("Your score is", t_score, "the higher lower game will only apply for the first game")
  else:
    t_score = t_score - p.scored
    print("Your score is now", chalk.green(t_score))
  #reflects on user performance and asks to play again.
  if t_score <= 0:
    print("You dont need to play again. Would you like to anyways?")
    replay_1 = input("")
    #if they want to play again, it resets all the variables that need to be reset for the program to run again.
    if replay_1.lower() == "yes":
      print("Good luck")
      A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} go extinct?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
      scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      yes = 0
      p.scored = 12
    else:
      #basically ends the program, this should be the last piece of text the user sees.
      print("Thank you for Playing. Goodbye.")
      break
  #reflecting again and encourages them to play again.
  elif t_score > 0:
    print("You can get a lower score! Would you like to play again?")
    replay_2 = input("")
    if replay_2.lower() == "yes":
      print("Good luck")
      A_1 = [f"What species is a {chalk.blue(CHALKS[0])}?", f"What species is a {chalk.blue(CHALKS[1])}", f"What species feeds primarily on {chalk.blue(CHALKS[2])} and {chalk.blue(CHALKS[3])}?", f"How many brains does an {chalk.blue(CHALKS[4])} have?", f"Is a {chalk.blue(CHALKS[5])} a fish?", f"In what war did {chalk.red(CHALKS[6])} pull out of?", f"In what war was {chalk.red(CHALKS[7])} in office?", f"How many years ago did the {chalk.red(CHALKS[8])} period end?", f"How many times did {chalk.red(CHALKS[9])} get stabbed?", f"Did {chalk.red(CHALKS[10])} start ww1?"]
      scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      yes = 0
      p.scored = 12
    else:
      print("Thank you for Playing. Goodbye.")
      break
#calm after the quiz, 60 seconds of an ascii art piece.
time.sleep(2)
os.system('clear')
print("""
   *  .  . *       *    .        .        .   *    ..
 .    *        .   ###     .      .        .            *
    *.   *        #####   .     *      *        *    .
  ____       *  ######### *    .  *      .        .  *   .
 /   /\  .     ###\#|#/###   ..    *    .      *  .  ..  *
/___/  ^8/      ###\|/###  *    *            .      *   *
|   ||%%(        # }|{  #
|___|,  \\  ejm    }|{""")
time.sleep(60)
os.system('clear')
