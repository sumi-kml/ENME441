from shifter import Shifter
import RPi.GPIO as GPIO
import time
import random
import threading

s1, s2, s3 = 16, 20, 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class Bug:
class Bug:
    def __init__(self, timestep=0.1, x=3, isWrapOn=False):
        self.timestep = timestep
        self.x = x
        self.isWrapOn = isWrapOn
        self.__shifter = Shifter(23, 25, 24)

    def start(self):
        pattern = 1 << self.x
        self.__shifter.shiftByte(pattern)

        step = random.choice([-1, 1])
        self.x += step

        if self.isWrapOn:
            self.x = self.x % 8
        else:
            self.x = max(0, min(7, self.x))

    def stop(self):
        self.__shifter.shiftByte(0)

b = Bug()

def flip(pin):
    b.isWrapOn = not b.isWrapOn

GPIO.add_event_detect(s2, GPIO.BOTH, callback=flip, bouncetime=500)
        
try:
    while True:
        if GPIO.input(s1):
            b.start()
        else:
            b.stop()

        if GPIO.input(s3):
            b.timestep = 0.1 / 3
        else:
            b.timestep = 0.1

        time.sleep(b.timestep)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()




    
