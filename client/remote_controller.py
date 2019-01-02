from tkinter import *
import tkinter.font as font
from gamepad import Gamepad
from time import sleep
from video_capture import VideoCapture
import PIL.Image, PIL.ImageTk

TITLE = 'Super RC'


class Window(Frame):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # update video every 15ms
        self.delay = 1

        top_frame = Frame(root, relief=RAISED, borderwidth=1)
        self.setup_video_frame(top_frame)
        top_frame.pack(fill=BOTH, expand=True)

        bottom_frame = Frame(root, relief=RAISED, borderwidth=1)
        bottom_frame.pack(fill=BOTH, expand=True)

        left_analog_frame = Frame(bottom_frame, relief=RAISED, borderwidth=1)
        digital_frame = Frame(bottom_frame, relief=RAISED, borderwidth=1, width=150)
        right_analog_frame = Frame(bottom_frame, relief=RAISED, borderwidth=1)

        left_analog_frame.pack(fill=BOTH, expand=True, side='left')
        digital_frame.pack(fill=BOTH, expand=True, side='left')
        right_analog_frame.pack(fill=BOTH, expand=True, side='left')

        digital_button_wrapper = Frame(digital_frame)
        digital_button_wrapper.pack(fill=NONE)
        digital_button_wrapper.place(relx=.5, rely=.5, anchor="c")

        # Digital buttons
        btn_font = font.Font(weight='bold')
        self.up_button = Button(digital_button_wrapper, text=u'\u2191', font=btn_font)
        self.up_button.pack(side=TOP, padx=5, pady=5)
        self.down_button = Button(digital_button_wrapper, text=u'\u2193', font=btn_font)
        self.down_button.pack(side=BOTTOM, padx=5, pady=5)
        self.left_button = Button(digital_button_wrapper, text=u'\u2190', font=btn_font)
        self.left_button.pack(side=LEFT, padx=5, pady=5)
        self.right_button = Button(digital_button_wrapper, text=u'\u2192', font=btn_font)
        self.right_button.pack(side=RIGHT, padx=5, pady=5)

        # Left analog bar
        self.left_analog = Scale(left_analog_frame, from_=10, to=-10)
        self.left_analog.set(0)
        self.left_analog.pack()
        self.left_analog.place(relx=.5, rely=.5, anchor="c")

        # Right analog bar
        self.right_analog = Scale(right_analog_frame, from_=10, to=-10)
        self.right_analog.set(0)
        self.right_analog.pack()
        self.right_analog.place(relx=.5, rely=.5, anchor="c")

        self.gamepad_thread = Gamepad(self)

        self.orig_color = self.up_button.cget('background')
        self.start_gamepad()

    def setup_video_frame(self, frame):
        self.video = VideoCapture()
        self.canvas = Canvas(frame, width=640, height=480)
        self.canvas.pack()
        self.update_video()

    def update_video(self):
        # Get a frame from the video source
        frame = self.video.get_frame()

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.root.after(self.delay, self.update_video)

    def update_left_analog(self, value):
        self.left_analog.set(value)

    def update_right_analog(self, value):
        self.right_analog.set(value)

    def update_digital(self, value):
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

    def set_status(self, value):
        self.root.title('{} - {}'.format(TITLE, value))

    def on_closing(self):
        self.gamepad_thread.stop()
        self.gamepad_thread.join()
        sleep(1)
        self.root.destroy()

    def start_gamepad(self):
        self.gamepad_thread.start()


def center(win):
    win.update_idletasks()
    width = 700
    height = 800
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2) - 50
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def main():
    root = Tk()
    root.title(TITLE)
    center(root)
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
