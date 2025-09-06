#FutureTime.py
#Name:Beau Pick
#Date:9-5-25
#Assignment:FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour =(now.hour - 5) %24
  currentMinute = now.minute

   #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
now = datetime.datetime.now()
currentHour =(now.hour - 17) %24
currentMinute = now.minute
Minute1= input ("Enter a minute amount")
Hour1 = input("Enter an Hour amount: ")
futureHour = (currentHour + int(Hour1)) %24 
futureMins =( currentMinute +int(Minute1)) %60
extraHour = ( currentMinute +int(Minute1)) //60

NowHour=( futureHour + extraHour) %12
print(NowHour, ":", futureMins)

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
