# time module have a very usefull function calld sleep() which can be used to delay the execution of a program for a specified amount of time.
# we will use that
import time

while True:
    # taking input from the user we need to ask how much time they want to set the timer for
    user_input = input("Enter the time in seconds (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        countdown_time = int(user_input)
        # DISPLAYING THE COUNTDOWN
        for s in range(countdown_time, 0, -1):
            seconds = s % 60
            minutes = (s // 60) % 60
            hours = s // 3600
            print(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            time.sleep(1)
        print("time's up!")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
