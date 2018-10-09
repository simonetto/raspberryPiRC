from tkinter import *
import tkinter.font as font


class Window(Frame):
    def __init__(self, root):
        super().__init__()

        top_frame = Frame(root, relief=RAISED, borderwidth=1, height=90)
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
        up_button = Button(digital_button_wrapper, text=u'\u2191', font=btn_font)
        up_button.pack(side=TOP, padx=5, pady=5)
        down_button = Button(digital_button_wrapper, text=u'\u2193', font=btn_font)
        down_button.pack(side=BOTTOM, padx=5, pady=5)
        left_button = Button(digital_button_wrapper, text=u'\u2190', font=btn_font)
        left_button.pack(side=LEFT, padx=5, pady=5)
        right_button = Button(digital_button_wrapper, text=u'\u2192', font=btn_font)
        right_button.pack(side=RIGHT, padx=5, pady=5)

        # Left analog bar
        left_analog = Scale(left_analog_frame, from_=-10, to=10)
        left_analog.set(0)
        left_analog.pack()
        left_analog.place(relx=.5, rely=.5, anchor="c")

        # Right analog bar
        right_analog = Scale(right_analog_frame, from_=-10, to=10)
        right_analog.set(0)
        right_analog.pack()
        right_analog.place(relx=.5, rely=.5, anchor="c")


def center(win):
    win.update_idletasks()
    width = 500
    height = 410
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2) - 50
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def main():
    root = Tk()
    root.title('Super RC')
    center(root)
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
