import pygame
import threading
from time import sleep


class Gamepad(threading.Thread):
    def __init__(self,
                 up_button,
                 down_button,
                 left_button,
                 right_button,
                 left_analog,
                 right_analog):
        threading.Thread.__init__(self)
        self.done = False
        self.up_button = up_button
        self.down_button = down_button
        self.left_button = left_button
        self.right_button = right_button
        self.left_analog = left_analog
        self.right_analog = right_analog
        self.orig_color = up_button.cget('background')

    def run(self):
        pygame.init()
        pygame.joystick.init()

        while self.done == False:
            pygame.event.get()
            joystick_count = pygame.joystick.get_count()

            if joystick_count > 0:
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

                self.update_left(joystick.get_axis(1))
                self.update_right(joystick.get_axis(3))
                self.update_camera(joystick.get_hat(0))

            sleep(0.05)
        pygame.quit()

    def update_left(self, value):
        self.left_analog.set(value * 10)

    def update_right(self, value):
        self.right_analog.set(value * 10)

    def update_camera(self, value):
        def paint_buttons(button1, button2, index):
            if value[index] == 0:
                button1.configure(bg=self.orig_color)
                button2.configure(bg=self.orig_color)
            elif value[index] == -1:
                button1.configure(bg='cyan')
                button2.configure(bg=self.orig_color)
            else:
                button1.configure(bg=self.orig_color)
                button2.configure(bg='cyan')

        paint_buttons(self.left_button, self.right_button, 0)
        paint_buttons(self.down_button, self.up_button, 1)

    def stop(self):
        self.done = True
