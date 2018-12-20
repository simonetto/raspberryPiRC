#!/usr/bin/python
import RPi.GPIO as GPIO #Import GPIO library
from espeak import espeak
import time
#Import time library
GPIO.setwarnings(False)
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(37,GPIO.OUT) # Trigger
GPIO.setup(24,GPIO.IN) # Echo
time.sleep(1)
print "Ultrasonic Measurement"
GPIO.output(37, False)

def measure():
time.sleep(0.333)
GPIO.output(37, True)
time.sleep(0.00001)
GPIO.output(37, False)
start = time.time()

while GPIO.input(24)==0:
start = time.time()

while GPIO.input(24)==1:
stop = time.time()

elapsed = stop-start
distance = (elapsed * 34300)/2
return distance
def stop():
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
def forward():
GPIO.output(7,True)
GPIO.output(11,False)
GPIO.output(13,True)
GPIO.output(15,False)
def back():
GPIO.output(7,False)
GPIO.output(11,True)
GPIO.output(13,False)
GPIO.output(15,True)
def left():
GPIO.output(7,True)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,True)
def right():
GPIO.output(7,False)
GPIO.output(11,True)
GPIO.output(13,True)
GPIO.output(15,False)
try:

while True:

distance = measure()
print "Distance : %.1f" % distance
time.sleep(0.0)
if distance >= 130:
forward()
else:
stop()
except KeyboardInterrupt:
#cleanup the GPIO pins before ending
GPIO.cleanup()