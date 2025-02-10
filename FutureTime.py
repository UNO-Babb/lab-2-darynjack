#FutureTime.py
#Name: Daryn
#Date: 02/01/2025
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute
  Question1 = input("What hour is it?")
  Question2 = input("What minute is it?")
  Question3 = input("How many hours into the future do you want to see?")
  Question4 = input("How many minutes into the future do you want to see?")
  #print (currentHour, currentMinute) #this is just for checking, we should delete it later
  currentHour = int(Question1)
  currentMinute = int(Question2)
  extraHour = (currentMinute + int(Question4))//60
  futureHour = (currentHour + int(Question3) + extraHour) % 24
  futureMinute = (currentMinute + int(Question4)) % 60
  #extraHour = (minuteCurrent + int(Question4))//60
  print(futureHour, ":", futureMinute)
  #TODO:
  #Ask user for hours
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

