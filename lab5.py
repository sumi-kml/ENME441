import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

pins = [17, 27, 22, 5, 6, 13, 19, 26, 21, 20]
base_f = 500
f = 0.2
phi = math.pi / 11

pwms = []
for p in pins:
    GPIO.setup(p, GPIO.OUT)
    pwm = GPIO.PWM(p, base_f)
    pwm.start(0)
    pwms.append(pwm)	

try:
	while 1:
		t = time.time()
		for i in range (10):
			phase = i * phi
			dc = (math.sin(2 * math.pi * f * t - phase)) ** 2
			pwms[i].ChangeDutyCycle(100 * dc)
except:
	GPIO.cleanup()


