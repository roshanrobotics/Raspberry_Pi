import time
import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
msg=""
i=0

while True:
    i+=1
    print("Counter{} - Hello from Raspberry Pi".format(i))
    ser.write('hello'.encode('utf-8'))
    time.sleep(2)

              
