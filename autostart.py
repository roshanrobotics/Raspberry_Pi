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
led=4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pir,GPIO.IN ,GPIO.PUD_DOWN)
GPIO.setup(mq,GPIO.IN)
GPIO.setup(buz,GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.output(buz,GPIO.LOW)
GPIO.output(light,GPIO.LOW)
GPIO.output(fan,GPIO.LOW)
GPIO.output(led,GPIO.LOW)
previous_state = False
current_state = False

#cam = picamera.PiCamera()  # new

api = ApiClient(token='BBFF-RJw1Qw7G69k54krU5l2WCjGnuxfpk7')
# Get a Ubidots Variable
#5e24a0b51d84724fa01853e1
button1 = api.get_variable('5e24a0b51d84724fa01853e1')                                              
button2 = api.get_variable('5e249fbd1d84724de38573d9')


lcd.static_text(0x80,"l","PCE ETC depart")
lcd.static_text(0xC0,"l","8th semester")
time.sleep(2)
lcd.lcd_byte(0x01,lcd.LCD_CMD)

lcd.static_text(0x80,"l","Smart Home")
lcd.static_text(0xC0,"l","Care System")
time.sleep(2)
lcd.lcd_byte(0x01,lcd.LCD_CMD)
INC=0

camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55


while True:
        last_value1 = button1.get_values(1)
        last_value2 = button2.get_values(1)
        print(last_value1[0]['value'])
        if last_value1[0]['value'] == 0.0:
                GPIO.output(light,GPIO.HIGH)
                lcd.static_text(0x80,"l","light 1 is off")
                print ("light off1")
                time.sleep(1.5)
                lcd.lcd_byte(0x01,lcd.LCD_CMD)
        
        elif last_value1[0]['value'] == 1.0:
                GPIO.output(light,GPIO.LOW)
                lcd.static_text(0x80,"l","light 1 is on")
                print ("light on1")
                time.sleep(1.5)
                lcd.lcd_byte(0x01,lcd.LCD_CMD)
                
                
        print(last_value2[0]['value'])
        if last_value2[0]['value'] == 1.0:
                GPIO.output(fan,GPIO.LOW)
                lcd.static_text(0xC0,"l","fan is on")
                print ("fan on2")
                time.sleep(1.5)
                lcd.lcd_byte(0x01,lcd.LCD_CMD)
                
        elif last_value2[0]['value'] == 0.0:
                GPIO.output(fan,GPIO.HIGH)
                lcd.static_text(0xC0,"l","fan is off")
                print ("fan off2")
                time.sleep(1.5)
                lcd.lcd_byte(0x01,lcd.LCD_CMD)
        
        if GPIO.input(mq)==False:
            print("gas detected")
            GPIO.output(buz,GPIO.HIGH)
            GPIO.output(led,GPIO.HIGH)
            lcd.static_text(0x80,"l","Alert")
            lcd.static_text(0xC0,"l","gas leakage")
            time.sleep(1.5)
            lcd.lcd_byte(0x01,lcd.LCD_CMD)
        else:
            GPIO.output(buz,GPIO.LOW)
            GPIO.output(led,GPIO.LOW)
            
            
                
        time.sleep(0.3)
        previous_state = current_state
        current_state = GPIO.input(pir)
        if current_state != previous_state:
            new_state = "HIGH" if current_state else "LOW"
            print("GPIO pin %s is %s" % (pir, new_state))
            if current_state:  # new
                #cam.start_preview()
                if INC==10:
                    INC=0
                INC +=1
                PATH='/home/pi/myvid/record'+str(INC)+'.h264'
                print("start while true")    
                print('Please Wait...')
                camera.start_recording(PATH)
                lcd.static_text(0x80,"l","Someone detected")
                time.sleep(10)
                camera.stop_recording()
                lcd.static_text(0x80,"l","Video recorded")
                lcd.static_text(0xC0,"l","successfully")
                print('Video recorded successfully')
                time.sleep(2)
                lcd.lcd_byte(0x01,lcd.LCD_CMD)
                
        else:
            previous_state = current_state
                    
        


               
                
  





