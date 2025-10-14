from shifter import Shifter
import time
import random

b = Shifter(23, 25, 24)

x = 0 

while True:
    pattern = 1 << x
    b.shiftByte(pattern)
    time.sleep(0.05)

    step = random.choice([-1, 1])
    x += step
    
    x = max(0, min(7, x))
