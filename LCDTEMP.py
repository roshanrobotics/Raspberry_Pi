import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
from AndyPi_LCD import AndyPi_LCD
lcd=AndyPi_LCD()
lcd.lcd_init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
while True:
        tempfile = open("/sys/bus/w1/devices/28-031644aed1ff/w1_slave")
        thetext = tempfile.read()
        tempfile.close()
        tempdata = thetext.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        t = temperature/1000
        print t
        lcd.static_text(0x80,"l","Temperature=  *C")
        lcd.lcd_byte(0x8C,lcd.LCD_CMD)
        lcd.lcd_int(int(t), 1)   
        
