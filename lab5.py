import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

p = 17
base_f = 500
f = 0.2

GPIO.setup(p, GPIO.OUT)

pwm = GPIO.PWM(p, base_f) 
pwm.start(0) 

try:
	while 1:
		t = time.time()
		b = (math.sin(2 * math.pi * f * t)) ** 2
		dc = b * 100  
		pwm.ChangeDutyCycle(dc)
except:
	GPIO.cleanup()



