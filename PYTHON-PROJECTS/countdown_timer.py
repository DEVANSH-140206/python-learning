# time module have a very usefull function calld sleep() which can be used to delay the execution of a program for a specified amount of time.
# we will use that
import time
# taking input from the user we need to ask how much time they want to set the timer for
countdown_time= int(input("Enter the time in seconds: "))
while(countdown_time == ""):
    print("Please enter a valid number.")
    countdown_time= int(input("Enter the time in seconds: "))
# DISPLAYING THE COUNTDOWN
for s in range (countdown_time,0,-1):
    seconds = s % 60
    minutes = (s /60)% 60
    hours = (s /3600)
    print(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    time.sleep(1)
print("time's up!")
