import pygame
import threading
from time import sleep
import time
from socketClient import SocketClient


class Gamepad(threading.Thread):
    def __init__(self, window):
        threading.Thread.__init__(self)
        self.done = False
        self.window = window
        self.socket = None
        self.socket = SocketClient('localhost', 10000, self.window.set_status)

    def run(self):
        self.socket.connect()

        if self.socket.is_connected:
            pygame.init()
            pygame.joystick.init()

            while not self.done:
                pygame.event.get()
                joystick_count = pygame.joystick.get_count()

                if joystick_count > 0:
                    joystick = pygame.joystick.Joystick(0)
                    joystick.init()

                    self.send_value(Gamepad.sanitize_digital(joystick.get_axis(1)), self.window.update_left_analog)
                    self.send_value(Gamepad.sanitize_digital(joystick.get_axis(3)), self.window.update_right_analog)
                    self.send_value(joystick.get_hat(0), self.window.update_digital)

                sleep(0.05)
            pygame.quit()

    @staticmethod
    def sanitize_digital(value):
        rounded = round(value * -10)
        if rounded == 1 or rounded == -1:
            return 0
        return rounded

    def send_value(self, value, callback):
        message = [value, int(round(time.time() * 1000))]
        self.socket.send(message, callback)

    def stop(self):
        self.socket.disconnect()
        self.window.set_status('Disconnected')
        self.done = True
