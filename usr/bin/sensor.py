#!/usr/bin/python3
# coding=utf-8
import Adafruit_DHT
# sensor type
sensor = Adafruit_DHT.DHT_11
# use BCM
pin=4
humidity,temperature = Adafruit_DHT.read(sensor,pin)
if humidity is not None and temperature is not None:
    print "temperature: %.2f" % temperature
    print "humidity: %.2f" % humidity
else:
    print "Fail! Please try again"
