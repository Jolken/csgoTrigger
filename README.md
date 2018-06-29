# Trigger for CS:GO
Simple trigger for CS:GO that can't be banned by VAC.
### How it works
This python script taking two screenshot of your crosshair and compare them. 
If they are different, it make shot.
Tested on Windows 10 x64, python 3.6.4.
### Usage
Look in the doorway, etc.
Press the hotkey, which you can change in the code.
Wait for the enemy.
If he was in your cross, the script would probably shoot and kill him :)
### Installation
Download zip archive or
```
$ git clone https://github.com/Jolken/csgoTrigger.git
```
Install packages
```
$ cd csgoTrigger
$ pip install -r requirements.txt
```
Or
```
$ pip install numpy
$ pip install Pillow
$ pip install opencv-python
$ pip install keyboard
```
Open console in CS:GO and bind +attack to fire key
```
> bind o +attack
```
Fire key can be changed in code.
### How to start
Open [trigger.py](trigger.py) with python or
```
$ python /.../csgoTrigger/trigger.py
```
### Change hotkey
Change the variable HOTKEY in [trigger.py](trigger.py). For example
```
HOTKEY = 'alt+r'
HOTKEY = 'q'
```
### Change fire key
Change the variable FIRE_KEY in [trigger.py](trigger.py). For example
```
FIRE_KEY = 0x18 #'O'
FIRE_KEY = 0x12 #'E'
FIRE_KEY = 0x4B # NUMPAD4
```
List of hex codes can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/bb321074(v=vs.85).aspx), [here](https://gist.github.com/tracend/912308) and [here](http://www.flint.jp/misc/?q=dik&lang=en).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
