# This is super easy to do in AHK, but I'm only doing this because I wanted to make an easy first non-course Project. Logic inspired by an AHK script from unknowncheats

import pyautogui
import numpy
import win32api
import win32con
from math import sqrt
from pynput import mouse
import psutil
import multiprocessing #multithreading was super slow idk why, maybe I didn't implement good enough


FOV_X = 100
FOV_Y = 100
MID_X = 960
MID_Y = 540
SCAN_X = MID_X - FOV_X
SCAN_Y = MID_Y - FOV_Y
REGION = (SCAN_X, SCAN_Y, FOV_X * 2, FOV_Y * 2)
TARGET_COLOR = (178, 109, 215)
COLOR_TOLERENCE = 10
UPPER_BOUND = numpy.array([TARGET_COLOR[0] + COLOR_TOLERENCE, TARGET_COLOR[1] + COLOR_TOLERENCE, TARGET_COLOR[2] + COLOR_TOLERENCE])
LOWER_BOUND = numpy.array([TARGET_COLOR[0] - COLOR_TOLERENCE, TARGET_COLOR[1] - COLOR_TOLERENCE, TARGET_COLOR[2] - COLOR_TOLERENCE])
OFFSET_X = 42 #42 
OFFSET_Y = 30 #30 
SKIP = 4
PID = win32api.GetCurrentProcessId()
PROCESS = psutil.Process(PID)
PROCESS.nice(psutil.HIGH_PRIORITY_CLASS)


def scan_screen():
    screen = pyautogui.screenshot(region=REGION)
    screen = screen.convert("RGB")
    screen_arr = numpy.array(screen)

    for y in range(0, screen_arr.shape[0], SKIP):
        for x in range(0, screen_arr.shape[1], SKIP):
            pixel = screen_arr[y, x]
            if numpy.all(pixel >= LOWER_BOUND) and numpy.all(pixel <= UPPER_BOUND):
                return (x+SCAN_X, y+SCAN_Y)
            
    return None


def move_mouse(target):
    target_x, target_y = target[0] + OFFSET_X, target[1] + OFFSET_Y

    relative_x = target_x - MID_X # x and y relative to the midpoint i.e. usually where the cursor is at in a game
    relative_y = target_y - MID_Y

    move_x = sqrt(abs(relative_x)) if relative_x > 0 else -sqrt(abs(relative_x))
    move_y = sqrt(abs(relative_y)) if relative_y > 0 else -sqrt(abs(relative_y))

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(move_x+1), int(move_y+1), 0, 0) # +1 to round it up


def lerp(target):
    target_x, target_y = target[0] + OFFSET_X, target[1] + OFFSET_Y

    
    

def move_if_running():
    global exit_program
    global moving

    while not exit_program.value:
        while moving.value:
            target = scan_screen()
            if target:
                move_mouse(target)


def check_input_listener(exit_program, moving):
    def on_click(x, y, button, pressed):
        if button.name == 'middle' and pressed:
            exit_program.value = True
            return False
        
        if not moving.value:
            if button.name == 'right' and pressed:
                moving.value = True
                return
            
        if moving.value:
            if button.name == 'right' and not pressed:
                moving.value = False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == "__main__":
    exit_program = multiprocessing.Value('b', False)
    moving = multiprocessing.Value('b', False)

    input_process = multiprocessing.Process(target=check_input_listener, args=(exit_program, moving))
    input_process.start()

    move_if_running()
    
    input_process.join()


