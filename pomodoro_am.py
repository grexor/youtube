import sys
import os
import time

pomodoro_start = 1

def countdown(t, b=False):
    while t>=0:
        mins, secs = divmod(t, 60)
        if not b:
            timer = "Pomodoro {pomodoro}".format(pomodoro=pomodoro) + "\n" + "{:02d}:{:02d}".format(mins, secs)
        else:
            timer = "Break" + "\n" + "{:02d}:{:02d}".format(mins, secs)
        f = open("pomodoro.txt", "wt")
        f.write(timer)
        f.close()
        time.sleep(1)
        t -= 1

pomodoro = pomodoro_start

while True:
    countdown(50*60)
    countdown(10*60, b=True)
    pomodoro += 1
