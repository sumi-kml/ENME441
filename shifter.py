import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110 

def ping(p):
  GPIO.output(p,1)
  time.sleep(0)
  GPIO.output(p,0)

def shiftByte(b): 
  for i in range(8):
    GPIO.output(dataPin, b & (1<<i))
    ping(clockPin) 
  ping(latchPin) 

try:
  shiftByte(0b01100110) 
  while 1: pass
except:
  GPIO.cleanup()  
