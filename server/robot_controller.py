import time
import RPi.GPIO as GPIO

FORWARD = 26
BACKWARD = 20
SLEEP_TIME = 1


# https://maker.pro/raspberry-pi/projects/make-obstacle-avoiding-robot-raspberry-pi
# https://maker.pro/raspberry-pi/tutorial/how-to-control-a-dc-motor-with-an-l298-controller-and-raspberry-pi
class RobotController:
    def __init__(self):
        self.mode = GPIO.getmode()
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(FORWARD, GPIO.OUT)
        GPIO.setup(BACKWARD, GPIO.OUT)

    def move(self, data):
        print(data)
        self.move_left()
        self.move_right()

    def move_left(self):
        print('moving left')

    def move_right(self):
        print('moving right')

    def move_forward(self, x):
        GPIO.output(FORWARD, GPIO.HIGH)
        print("Moving Forward")
        time.sleep(x)
        GPIO.output(FORWARD, GPIO.LOW)

    def move_reverse(self, x):
        GPIO.output(BACKWARD, GPIO.HIGH)
        print("Moving Backward")
        time.sleep(x)
        GPIO.output(BACKWARD, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()
