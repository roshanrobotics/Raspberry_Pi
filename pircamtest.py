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
#def record_video(PAT):



camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    print(current_state)
    if current_state != previous_state:
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
    #record_video(PATH)
       #time.sleep(1)
        print("1st video done")
        previous_state = current_state
    else:
        previous_state = current_state
        
        #new_state = "HIGH" if current_state else "LOW"
        #print("GPIO pin %s is %s" % (sensor, new_state))
'''if current_state:  # new
    #cam.start_preview()
    camera.start_recording()
    #time.sleep(10)
else:
    #cam.stop_preview()
    camera.stop_recording()
    print('Video recorded successfully')
    time.sleep(2)'''
