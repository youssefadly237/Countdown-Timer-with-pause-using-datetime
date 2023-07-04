'''
countdown timer with pause using datetime
by Youssef Adly
'''

from datetime import datetime, timedelta
from time import sleep
import keyboard

# Collect user input for the duration of the timer
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
s = int(input("Enter Seconds: "))

# Calculate the future time by adding the duration to the current time
add_val = timedelta(hours=h, minutes=m, seconds=s)
now = datetime.now()
future_time = now + add_val

check = False
timer_status = True

def update_timer_status():
    """
    Update the timer status based on the user keyboard input.
    """
    global timer_status
    if keyboard.is_pressed('p'):
        timer_status = False  # Pause the timer
    elif keyboard.is_pressed('s'):
        timer_status = True  # Start or resume the timer

while now < future_time:
    update_timer_status()
    now = datetime.now()  # Update the current time
    if timer_status and not check:
        remain = future_time - now
        print("Remaining Time:", remain)
        sleep(1)
    elif not timer_status and not check:
        remain = future_time - now
        print("Timer paused")
        check = True
    elif timer_status and check:
        future_time = now + remain
        print("Remaining Time:", remain)
        sleep(1)
        check = False
    else:
        pass
