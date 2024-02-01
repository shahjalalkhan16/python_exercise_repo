## Countdown Timer: Create a countdown timer from 10 to 0 using a while loop.
import time
countdown = 10

while countdown >= 0:
    print(countdown, end="\n")
    countdown -= 1
    time.sleep(1)


