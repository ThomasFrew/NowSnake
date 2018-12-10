#Imports the neccessary functions
from datetime import *
from time import *
from re import *

#Derives all neccessary variables (core)
firstiteration = True
actionunresolved = True

action = "undefined"
setup = "undefined"

weekday = "undefined"
month = "underfined"
meridiem = "undefined"
secondnum = "undefined"
minutenum = "undefined"
microsecondnum = "undefined"
hournum = "undefined"
monthnum = "undefined"
daynum = "undefined"
yearnum = "undefined"
daysuffix = "undefined"

def update():
     global weekday
     global month
     global meridiem
     global secondnum
     global minutenum
     global microsecondnum
     global hournum
     global monthnum
     global daynum
     global yearnum
     global daysuffix

#Sets up the "now" object
     now = datetime.today()

#Derives all neccessary variables (unprocessed time)
     weekday = now.strftime("%A")
     month = now.strftime("%B")
     meridiem = now.strftime("%p")
     secondnum = now.strftime("%S")
     minutenum = now.strftime("%M")

#Derives all neccessary variables (processed time)
     microsecondnum = now.strftime("%f")[4:6]
     while microsecondnum[0] == "0" and len(microsecondnum) > 1:
          microsecondnum = microsecondnum[1:]
     
     hournum = now.strftime("%I")
     while hournum[0] == "0":
         hournum = hournum[1:]
     
     monthnum = now.strftime("%m")
     while monthnum[0] == "0":
          monthnum = monthnum[1:]

     daynum = now.strftime("%d") 
     while daynum[0] == "0":
          daynum = daynum[1:]

     yearnum = now.strftime("%Y")
     while yearnum[0] == "0" and len(yearnum) > 1:
          yearnum = yearnum[1:]

#Derives other, dependent variables
     if daynum[-1] == "1":
         daysuffix = "st"
     elif daynum[-1] == "2":
         daysuffix = "nd"
     elif daynum[-1] == "3":
        daysuffix = "rd"
     else:
         daysuffix = "th"



#Sets up a fuction to request user input
def request():
     global firstiteration
     global actionunresolved
     global action
     global setup

     actionunresolved = True
     
     if firstiteration == True:
          print("Welcome to NowSnake: The python program needed for all things time!")
          sleep(0.5)
          action = input("Would you like a Full or Condensed Setup? (F/C)" + "\n" + ">>>")
          
          while actionunresolved == True:
               if action != "F" and action != "C" and action != "f" and action != "c":
                    action = input("Please respond with either (F/C) to signify whether you a full or condensed setup." + "\n" + ">>>")
               else:
                    actionunresolved = False
          firstiteration = False
          print("\n")
          
     elif firstiteration == False:
          action = input("Would you like to update or change setups? (U/F/C)" + "\n" + ">>>")
     
          while actionunresolved == True:
               if action != "F" and action != "C" and action != "f" and action != "c" and action != "U" and action != "u":
                    action = input("Please respond with either (U/F/C) to signify whether you want to update tor change setups." + "\n" + ">>>")
               else:
                    actionunresolved = False
          print("\n")

     else:
          print("DeD")
     
#Decides which setup to render
def render():
     global firstiteration
     global actionunresolved
     global action
     global setup
     
     if action == "U" or action == "u":
          if setup == "F" or setup == "f":
               print("Updating...")
               sleep(1.5)
               fullsetup()
     
          elif setup == "C" or setup == "c":
               print("Updating...")
               sleep(0.5)
               condensedsetup()

          else:
               print("Error 004: Update Type Error!")
     
     elif action == "F" or action == "f":
          setup = "F"
          print("Rendering...")
          sleep(1.5)
          fullsetup()

     elif action == "C" or action == "c":
          setup = "C"
          print("Rendering...")
          sleep(0.5)
          condensedsetup()
     
     else:
          print("Error 005: Confugration Type Error!")
     
#Renders full setup
def fullsetup():
     global weekday
     global month
     global meridiem
     global secondnum
     global minutenum
     global microsecondnum
     global hournum
     global monthnum
     global daynum
     global yearnum
     global daysuffix
     
     print("Today is", weekday, "the", daynum + daysuffix, "of", month, yearnum + ".")
     sleep(0.5)
     print("In Australian notation, this equates to", daynum + "/" + monthnum + "/" + yearnum + ".")
     sleep(0.5)
     print("The time is precisely", hournum + ":" + minutenum + ":" + secondnum + "." + microsecondnum, meridiem + ".")
     sleep(0.5)
     greet()
     sleep(0.5)

#Renders condensed setup
def condensedsetup():
     global weekday
     global meridiem
     global secondnum
     global minutenum
     global hournum
     global monthnum
     global daynum
     global yearnum
     
     print("It's", daynum + "/" + monthnum + "/" + yearnum + ",", "a", weekday + ".")
     sleep(0.5)
     print("It's", hournum + ":" + minutenum + ":" + secondnum, meridiem + ".")
     sleep(0.5)

#Greets the user depending on the current time (full setup)
def greet():
     global hournum
     
     if int ((hournum) == 12 or int(hournum) < 4) and meridiem == "AM":
          print("Hope you're having a good night. Maybe you should get some sleep!")
     elif int(hournum) >= 4 and int(hournum) < 12 and meridiem == "AM":
          print("Top of the morning! Did you know that you are most productive between 8:00 AM and 2:00 PM? This gives you about", (12 - int(hournum)) + 2, "hour(s) left of optimal productivity!")
     elif (int(hournum) == 12 or int(hournum) < 4) and meridiem == "PM":
          print("Afternoon! Is it time for lunch? Well, people from timezones CST to NZT typically have lunch around this time: this stretches from China to New Zealand!")
     elif int(hournum) > 4 and meridiem == "PM":
          if int(hournum) < 7:
               print("Good evening. Did you know that the peak time for electricity usage is 7:00 PM? This makes you about", (7 - int(hournum)), "hour(s) away from that time!")
          elif int(hournum) >= 7:
               print("Good evening. Did you know that the peak time for electricity usage is 7:00 PM? This makes you about", (int(hournum) - 7), "hour(s) away from that time!")
          else:
               print("Error 003: Advanced Evening Time Derivative Error!")
     else:
          print("Error 002: General Time Derivative Error!")

#Main loop
while True:
     update()
     request()
     render()
     

    
    

