import time
from time import sleep

def clock(hours, seconds, minutes):
    while True:
        seconds += 1
        sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                hours += 1
def showClock():
    


