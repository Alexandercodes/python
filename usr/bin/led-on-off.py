#!usr/bin/python3
import RPi.GPIO as gpio 
import time

#  use the pin-numberg
gpio.setmode(gpio.BOARD)

# pin 26 should be used as data output
gpio.setup(26,gpio.OUT)

#turn LED eight times on and off
for i in range(8):
	gpio.output(26,gpio.HIGH)
	time.sleep(1)
	gpio.output(26,gpio.LOW)
	time.sleep(1)

#release all GPIO-Pins
gpio.cleanup()
