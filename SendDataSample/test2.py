import serial
ser = serial.Serial('/dev/ttyS0', 9600)
print('hola')
while True:
    incoming = ser.readline().strip()
    print ('hola')
    
