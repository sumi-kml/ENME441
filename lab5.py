import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

p1 = 17
p2 = 27
base_f = 500
f = 0.2
phi = math.pi / 11

GPIO.setup(p1, GPIO.OUT)
GPIO.setup(p2, GPIO.OUT)

pwm1 = GPIO.PWM(p1, base_f) 
pwm2 = GPIO.PWM(p2, base_f) 
pwm1.start(0) 
pwm2.start(0) 

try:
	while 1:
		t = time.time()
		b1 = (math.sin(2 * math.pi * f * t)) ** 2
		b2 = (math.sin(2 * math.pi * f * t - phi)) ** 2 
		pwm1.ChangeDutyCycle(100 * b1)
		pwm2.ChangeDutyCycle(100 * b2)
except:
	GPIO.cleanup()

