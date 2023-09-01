import RPi.GPIO as GPIO
import time
import picamera  # new

sensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

camera= picamera.PiCamera()  # new
INC=0
while True:
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
            


