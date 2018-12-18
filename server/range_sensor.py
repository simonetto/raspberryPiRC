import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
SOUND_SPEED = 17150


class RangeSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.output(TRIG, False)
        print('Waiting For Sensor To Settle')
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        self.pulse_start = 0
        self.pulse_end = 0

    def get_distance(self):
        while GPIO.input(ECHO) == 0:
            self.pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            self.pulse_end = time.time()

        pulse_duration = self.pulse_end - self.pulse_start
        distance = pulse_duration * SOUND_SPEED
        return round(distance, 2)

    def can_move_forward(self):
        return self.get_distance() > 10

    def __del__(self):
        GPIO.cleanup()
