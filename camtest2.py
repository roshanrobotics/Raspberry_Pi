import RPi.GPIO as GPIO
import time
import picamera  # new

sensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

#cam = picamera.PiCamera()  # new
INC=0
def record_video(PAT):
        print('Please Wait...')
        camera.start_recording(PAT)
        time.sleep(10)
        camera.stop_recording()
        print('Video recorded successfully')

        time.sleep(2)


camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH"
        print("GPIO pin %s is %s" % (sensor, new_state))
        if current_state:
            if INC==10:
                INC=0     
            PATH='/home/pi/myvid/ash'+str(INC)+'.h264'
            print("start while true")
            record_video(PATH)
            time.sleep(1)
            print("1st video done")
            INC +=1
            
    else:"LOW"
            

