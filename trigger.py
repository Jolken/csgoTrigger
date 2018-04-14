import numpy as np
from PIL import ImageGrab
from cv2 import cvtColor, COLOR_BGR2GRAY, Canny
import time
import keyboard
import winsound
from directkeys import PressKey, ReleaseKey

screenShot = ImageGrab.grab()
HALF_WIDTH = screenShot.size[0]/2
HALF_HEIGHT = screenShot.size[1]/2 
HOTKEY = 'shift+z'
FIRE_KEY = 0x18 #key codes --> https://msdn.microsoft.com/en-us/library/windows/desktop/bb321074(v=vs.85).aspx 
SHOTS_NUMBER = 5
del screenShot
isEnabled = False

def inverseIsEnabled():
    global isEnabled
    if isEnabled:
        winsound.Beep(1000, 200)
        print('Disabled')
        isEnabled = False
    else:
        winsound.Beep(500, 200)
        print('Enabled')
        isEnabled = True

#Detect edges in image
def processImg(image):
    return Canny(cvtColor(image, COLOR_BGR2GRAY), threshold1=0, threshold2=100)

def makeFire():
    for x in range(SHOTS_NUMBER):
        PressKey(FIRE_KEY)
        time.sleep(0.1)
        ReleaseKey(FIRE_KEY)
        time.sleep(0.05)
    del x

def takeCrosshair():
    return np.array(ImageGrab.grab(bbox=(HALF_WIDTH-5, HALF_HEIGHT-5, HALF_WIDTH+5, HALF_HEIGHT+5)))

def trigger():
    while True:
        if isEnabled:
            crosshair1 = processImg(takeCrosshair())
            time.sleep(0.00000000001)
            crosshair2 = processImg(takeCrosshair())
            if (crosshair1 != crosshair2).any():
                makeFire()
                inverseIsEnabled()
                
if __name__ == '__main__':
    keyboard.add_hotkey(HOTKEY, inverseIsEnabled)
    print('Press '+HOTKEY+' to enable cheat for '+str(SHOTS_NUMBER)+' shots')
    trigger()
