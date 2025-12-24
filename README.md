# color_aimbot
Simple AHK-like color aimbot(currently only for Krunker) script in python, as my first non-course project

## Requirements
To run this program, you'll need to install the following libraries:
- keyboard
- numpy
- pyautogui
- pynput
- pywin32
- pillow
- psutil


You can install them by running the following command in your terminal
```bash
pip install -r requirements.txt
```

## How to Run the Script
Run aimbot.py silently using the following command:
```bash
pythonw.exe aimbot.py
```

## How to Start Aimbotting in Krunker
Set your krunker UI scale to 0.7 and the Nametag type to any Non-Simple type and set nametag scale to 1. Then get the RGB values of your Enemy healthbar and Change the value of TARGET_COLOR constant in the script to your color in the format (R, G, B).  
For Simple type nametags Change the OFFSET_X constant to 0 and OFFSET_Y constant to around 10 and follow the above steps for Color

Aimbot triggers with Right Click

Middle-Mouse button to end the Script

