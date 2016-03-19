#!/usr/bin/python3
# file name: steuerung.py

import os
import time
while True:
    lt=time.localtime()
    h = lt[3]
# now: steuerung

if h <=20 and h >=8:
    os.system("sudo /home/pi/reswitch-pi/./send 10100 4 1")
    print("before 7 o'clock - on")
else
    os.system("sudo /home/pi/reswitch-pi/./send 10100 4 0")

time.sleep (60)
