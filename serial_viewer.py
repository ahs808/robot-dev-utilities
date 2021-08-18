#!/usr/bin/env python3

'''
Simple script to print the output from a streaming serial 
device to the terminal. Useful in troubleshooting a serial 
device especially on a machine that may not have access to 
internet and does not have a serial terminal program already
installed such as minicom or gtkterm.

Make sure you set appropriate port and baud rate for the 
serial device.

github.com/ahs808
'''

import time
import serial

port = '/dev/ttyACM0'
baud = 9600

eol = ['\r','\n','\n\r','\r\n']

ser = serial.Serial(port,baud)
out = ''

try:
    while True:
        while ser.inWaiting() > 0:
            last_char = ser.read(1).decode('utf-8')
            out += str(last_char)
            if str(last_char) in eol:
                print(out)
        time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()