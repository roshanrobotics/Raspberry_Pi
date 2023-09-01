import RPi.GPIO as GPIO 
import picamera
from ubidots import ApiClient
import time

sensor=17
mq=22
buz=27
light=26
fan=19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor,GPIO.IN ,GPIO.PUD_DOWN)
GPIO.setup(mq,GPIO.IN)
GPIO.setup(buz,GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
GPIO.output(buz,GPIO.LOW)
GPIO.output(light,GPIO.LOW)
GPIO.output(fan,GPIO.LOW)
previous_state = False
current_state = False

#cam = picamera.PiCamera()  # new

api = ApiClient(token='BBFF-RJw1Qw7G69k54krU5l2WCjGnuxfpk7')
# Get a Ubidots Variable
#5e24a0b51d84724fa01853e1
button1 = api.get_variable('5e24a0b51d84724fa01853e1')                                              
button2 = api.get_variable('5e249fbd1d84724de38573d9')

INC=0
#def record_video(PAT):


       # time.sleep(2)


camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55


INC=0
def video_record():
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
        if current_state:  # new
            #cam.start_preview()
            if INC==10:
                INC=0
            INC +=1
            PATH='/home/pi/myvid/record'+str(INC)+'.h264'
            print("start while true")    
            print('Please Wait...')
            camera.start_recording(PATH)
            time.sleep(10)
            camera.stop_recording()
            
            print('Video recorded successfully')
            time.sleep(2)
        else:
            previous_state = current_state
            print("else")
while True:
        video_record()
        last_value1 = button1.get_values(1)
        last_value2 = button2.get_values(1)
        print(last_value1[0]['value'])
        if last_value1[0]['value'] == 1.0:
                GPIO.output(light,GPIO.HIGH)
                print ("on1")
        
        elif last_value1[0]['value'] == 0.0:
                GPIO.output(light,GPIO.LOW)
                
                print ("off1")
        print(last_value2[0]['value'])
        if last_value2[0]['value'] == 0.0:
                GPIO.output(fan,GPIO.LOW)
                
                print ("off2")
                
        elif last_value2[0]['value'] == 1.0:
                GPIO.output(fan,GPIO.HIGH)
                
                print ("on2")
        
        elif GPIO.input(mq)==False:
                print("gas detected")
                GPIO.output(buz,GPIO.HIGH)
                

        


               
                
  





