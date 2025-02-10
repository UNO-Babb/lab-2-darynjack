#FutureTime.py
#Name: Daryn
#Date: 02/01/2025
#Assignment: Lab 2

# datetime will allow us to access the system date and time.

from now import now
currentHour = ("2")
currentMinute = ("07")
datetime = ("2/2/2025")
extraHour = (" + 1 hour")
futureMins = ("13")
def main():

#getting current time from system, storing to variable

now =  datetime.now(2//13)
currentHour = (now.hour - 5) % 24
currentMinute = (now.minute)
print ("currentHour") # type: ignore
print ("currentMinute")
print ("currentHour" ,  "currentMinute")
  #TODO:
  #Ask user for hours
  #Ask user for minutes
moreMins = 5

futureMins = ( currentMinute + moreMins ) % 60
extraHour = (currentMinute + moreMins ) // 60
print(extraHour)


print(futureMins)
  

if __name__ == '__main__':
  main(2//13)
