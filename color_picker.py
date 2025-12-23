import pyautogui
import numpy
import keyboard
import tkinter as tk


def show_window(color): 
    window = tk.Tk()
    window.title("My First Python Window") 
    window.geometry("200x100")
    label = tk.Label(window, text=f"{color}")
    label.pack()
    window.mainloop()

def get_color(position: tuple):
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert()
    image_array = numpy.array(screenshot)
    position_color = image_array[position[1], position[0]]
    return position_color

def on_key_press(event):
    if event.name == 'v':
        position = pyautogui.position()
        print(position)
        color = get_color(position)
        show_window(color)
        
    elif event.name == 'q':
            print("Quitting...")
            keyboard.unhook_all()
            exit()

keyboard.on_press(on_key_press)

keyboard.wait('q')
