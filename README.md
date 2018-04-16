# Trigger for CS:GO
Simple trigger for CS:GO that can't be banned by VAC.
### How it works
This python script taking two screenshot of your crosshair and compare them. 
If they are different, it make shot.
Tested on Windows 10 x64, python 3.6.4.
### Usage
Look in the doorway, etc.
Press the hot key, which you can change in the code.
Wait for the enemy.
If he was in your cross, the script would probably shoot and kill him :)
### Installation
Download zip archive or
```
$ git clone https://github.com/Jolken/csgoTrigger
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
### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details