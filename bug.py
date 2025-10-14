from shifter import Shifter
import time
import random

b = Shifter(23, 25, 24)

x = 0 

while True:
    pattern = 1 << position
    b.shiftByte(pattern)
    time.sleep(0.05)

    step = random.choice([-1, 1])
    position += step

    position = max(0, min(7, position))

try:
  b = Shifter(23, 25, 24)
  b.shiftByte(0b01100111)
  while 1: pass
except:
  GPIO.cleanup()  
