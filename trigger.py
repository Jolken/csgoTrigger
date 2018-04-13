import numpy as np
from PIL import ImageGrab
import cv2
import time
import keyboard
import winsound
from directkeys import PressKey, ReleaseKey

WIDTH = ImageGrab.grab().size[0]/2
HEIGHT = ImageGrab.grab().size[1]/2 
HOTKEY = 'shift+z'
FIRE_KEY = 0x18
SHOTS_NUMBER = 5
def inverse_enable():
    global enable
    if enable:
        winsound.Beep(1000, 200)
        print('Disabled')
        enable = False
    else:
        winsound.Beep(500, 200)
        print('Enabled')
        enable = True

def process_img(image):
    return cv2.Canny(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), threshold1=100, threshold2=200)

def makeFire():
    for i in range(SHOTS_NUMBER):
        PressKey(FIRE_KEY)
        time.sleep(0.1)
        ReleaseKey(FIRE_KEY)
        time.sleep(0.05)

def main():
    print('Press '+HOTKEY+' to enable cheat for '+str(SHOTS_NUMBER)+' shots')
    while True:
        if enable:
            screen1 = process_img(np.array(ImageGrab.grab(bbox=(WIDTH-10, HEIGHT-10, WIDTH+10, HEIGHT+10))))
            time.sleep(0.00000000001)
            screen2 = process_img(np.array(ImageGrab.grab(bbox=(WIDTH-10, HEIGHT-10, WIDTH+10, HEIGHT+10))))
            if (screen1 != screen2).any():
                makeFire()
                inverse_enable()
                




if __name__ == '__main__':
    enable = False
    img = ImageGrab.grab()
    keyboard.add_hotkey(HOTKEY, inverse_enable)
    main()
