import RPi.GPIO as GPIO 
import picamera
from ubidots import ApiClient
import time
from AndyPi_LCD import AndyPi_LCD
lcd=AndyPi_LCD()
lcd.lcd_init()
pir=17
mq=22
buz=27
light=26
fan=19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pir,GPIO.IN)
GPIO.setup(mq,GPIO.IN)
GPIO.setup(buz,GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
GPIO.output(buz,GPIO.LOW)
GPIO.output(light,GPIO.LOW)
GPIO.output(fan,GPIO.LOW)

api = ApiClient(token='BBFF-RJw1Qw7G69k54krU5l2WCjGnuxfpk7')
# Get a Ubidots Variable
#5e24a0b51d84724fa01853e1
button1 = api.get_variable('5e24a0b51d84724fa01853e1')                                              
button2 = api.get_variable('5e249fbd1d84724de38573d9')
lcd.static_text(0x80,"l","PCE ETC depart")
lcd.static_text(0xC0,"l","8th semester")
time.sleep(1)
lcd.lcd_byte(0x01,lcd.LCD_CMD)

lcd.static_text(0x80,"l","Home automation")
lcd.static_text(0xC0,"l","system")
time.sleep(1)
lcd.lcd_byte(0x01,lcd.LCD_CMD)

#lcd.lcd_byte(0x8C,lcd.LCD_CMD)
INC=0
def record_video(PAT):
        print('Please Wait...')
        camera.start_recording(PAT)
        time.sleep(10)
        camera.stop_recording()
        print('Video recorded successfully')
        lcd.static_text(0x80,"l","Video recorded")
        lcd.static_text(0xC0,"l","successfully")
        time.sleep(2)


camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55


'''try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            GPIO.output(24, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()'''

while True:
        last_value1 = button1.get_values(1)
        last_value2 = button2.get_values(1)
        print(last_value1[0]['value'])
        if last_value1[0]['value'] == 1.0:
                GPIO.output(light,GPIO.HIGH)
                #lcd.static_text(line, “justification”, “Static Message”)
                lcd.static_text(0x80,"l","light 1 is on")
                print ("on1")
        
        elif last_value1[0]['value'] == 0.0:
                GPIO.output(light,GPIO.LOW)
                lcd.static_text(0x80,"l","light 1 is off")
                print ("off1")
        print(last_value2[0]['value'])
        if last_value2[0]['value'] == 0.0:
                GPIO.output(fan,GPIO.LOW)
                lcd.static_text(0x80,"l","fan is on")
                print ("off2")
                
        elif last_value2[0]['value'] == 1.0:
                GPIO.output(fan,GPIO.HIGH)
                lcd.static_text(0x80,"l","fan is off")
                print ("on2")
        
        if GPIO.input(mq)==False:
                GPIO.output(buz,GPIO.HIGH)
                lcd.static_text(0x80,"l","Alert")
                lcd.static_text(0xC0,"l","gas leakage")
        time.sleep(2)
        if GPIO.input(pir)==False:
                if INC==10:
                        INC=0
                lcd.static_text(0x80,"l","Alert theft detected")
                PATH='/home/pi/myvid/rec'+str(INC)+'.h264'
                print("start while true")
                record_video(PATH)
                time.sleep(1)
                print("1st video done")
                INC +=1
        time.sleep(0.1)
        


               
                
  





