import RPi.GPIO as GPIO
import time

class Shifter:
  def __init__(self, serialPin, clockPin, latchPin):
    self.serialPin = serialPin
    self.latchPin = latchPin
    self.clockPin = clockPin
    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(self.serialPin, GPIO.OUT)
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

    pattern = 0b01100110 
    
  def __ping(self, p):
    GPIO.output(p,1)
    time.sleep(0)
    GPIO.output(p,0)

  def shiftByte(self, b): 
    for i in range(8):
      GPIO.output(self.serialPin, b & (1<<i))
      self.__ping(self.clockPin) 
    self.__ping(self.latchPin) 

try:
  a = Shifter(23, 25, 24)
  a.shiftByte(0b01100110)
  while 1: pass
except:
  GPIO.cleanup()  
