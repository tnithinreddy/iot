import RPi.GPIO as GPIO
import time
num=7
input=18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(input, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(num, GPIO.OUT)         #LED output pin
for j in range(1,5000):
       time.sleep(0.1)
       i=GPIO.input(input)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             GPIO.output(num, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(num, 1)  #Turn ON LED
             time.sleep(0.1)
GPIO.cleanup()