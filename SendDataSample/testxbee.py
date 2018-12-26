import serial, time, datetime, sys
#from xbee import XBee
from digi.xbee.devices import XBeeDevice
#from xbee import ZigBee
#import subprocess
#import pprint
#import MySQLdb
#import chat


SERIALPORT = '/dev/ttyS0'
BAUDRATE = 9600

ser = serial.Serial(SERIALPORT, BAUDRATE)

xbee = XBee(ser)

print ('Starting Up XBee Monitor')
# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print (response)
    except KeyboardInterrupt:
        break

ser.close()
