import RPi.GPIO as GPIO
import time

light=26
fan=19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(light,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
#GPIO.output(buz,GPIO.LOW)
GPIO.output(light,GPIO.LOW)
GPIO.output(fan,GPIO.LOW)

while True:
    GPIO.output(fan,GPIO.HIGH)
    GPIO.output(light,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(fan,GPIO.LOW)
    GPIO.output(light,GPIO.LOW)
    time.sleep(1)    
