#!/usr/bin/python

import tkinter as tk
import tkinter.font as font
import simpleaudio as sa
import os
import sys
import shutil

counter = 1
stop, skip = False, False
play_obj, wave_obj = None, None
filenames = None
file = None


def init():
    global counter, filenames, filename
    filenames = os.walk(path)
    filenames = list(filenames)[0][-1]
    for item in filenames:
        if item.split('.')[-1] != "wav":
            filenames.remove(item)
    if not filenames:
        return False
    counter = set_counter()
    next_file()
    return True


def set_counter():
    counter = 0
    recorded = os.walk(dst)
    recorded = list(recorded)[0][-1]
    for item in recorded:
        if item.split('.')[-1] != "wav":
            recorded.remove(item)
    recorded = [int(x.split('_')[0]) for x in recorded]
    if not(recorded):
        return counter
    counter = max(recorded)
    return counter


def next_file():
    global skip, filenames, filename, counter
    counter += 1
    if filenames:
        filename = path + filenames.pop()
    else:
        filename = None
    skip = False


def on_closing():
    global stop, window
    stop = True
    window.destroy()
    return


def main():
    global filename, play_obj, wave_obj, skip

    if play_obj is None:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
    elif skip:
        play_obj.stop()
        play_obj = None
        skip = False
        if not(filenames):
            return
        next_file()
    elif not(play_obj.is_playing()):
        play_obj = None
    elif stop:
        return


def show_msg_male():
    global skip
    skip = True
    shutil.move(filename, dst + f'{counter}_M.wav')


def show_msg_female():
    global skip
    skip = True
    shutil.move(filename, dst + f'{counter}_K.wav')


def show_msg_idk():
    global skip
    skip = True
    os.remove(filename)
    return


window = tk.Tk()
window.title("Classify voice by gender")
window.geometry("500x500")
window.attributes('-zoomed', True)

# Specify Grid
tk.Grid.rowconfigure(window, 0, weight=1)
tk.Grid.columnconfigure(window, 0, weight=1)

tk.Grid.rowconfigure(window, 1, weight=1)
tk.Grid.rowconfigure(window, 2, weight=1)

# Create Buttons
button_1 = tk.Button(window, text="Male", bg='#429bdb', fg="white",
                     activebackground='#429bdB', activeforeground="white",
                     command=show_msg_male)
button_2 = tk.Button(window, text="Female", bg='#db3773', fg="white",
                     activebackground="#db3773", activeforeground="white",
                     command=show_msg_female)
button_3 = tk.Button(window, text="IDK", bg='grey', fg="white",
                     activebackground="grey", activeforeground="white",
                     command=show_msg_idk)

# Define font
myFont = font.Font(family='Helvetica', size=20, weight='bold')
button_1['font'] = myFont
button_2['font'] = myFont
button_3['font'] = myFont

# Set grid
button_1.grid(row=0, column=0, sticky="NSEW")
button_2.grid(row=1, column=0, sticky="NSEW")
button_3.grid(row=2, column=0, sticky="NSEW")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"ERROR: Use '{sys.argv[0]} <src-folder> <dst-folder>' instead")
    else:
        global path, dst
        path = sys.argv[1]
        dst = sys.argv[2]
        if path[-1] != "/":
            path += "/"
        if dst[-1] != "/":
            dst += "/"

        init()
        window.protocol("WM_DELETE_WINDOW", on_closing)
        while True:
            main()
            if stop:
                break
            window.update()
        window.mainloop()
