#Magic8Ball.py
#Name: Daryn
#Date: 02/01/2025
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
    #Prompt the user for their question.
  Question = input("What do you want to know?")
  answer = ["Yes absolutely" , "No not at all" , "As I see it, yes" , "Ask again later" , "Better not tell you now" , "Cannot predict now" , "Most likely" ,
           "It is certain" , "My reply is no" , "My sources say no" , "Outlook good" , "Outlook not good" , "My reply is no" , "Try again later" , 
           "Odds are not good" , "Odds are in your favor" , "Probably not" , "Go for it" , "Sounds good" , "No"]
 #Answer question randomly with one of the options from your earlier list.
  length = len(answer)
  r = random.random() * length

  r = int(r) #cut off any decimal values

  spot = r
  print(answer[spot])

if __name__ == '__main__':
  main()
