import RPi.GPIO as GPIO 
import picamera
import time
pir=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pir,GPIO.IN ,GPIO.PUD_DOWN)

# GPIO.output(led,GPIO.LOW)
previous_state = False
current_state = False

#cam = picamera.PiCamera()  # new
INC=0
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55


while True:
        time.sleep(0.1)
        previous_state = current_state
        current_state = GPIO.input(pir)
        if current_state != previous_state:
            new_state = "HIGH" if current_state else "LOW"
            #print("GPIO pin %s is %s" % (pir, new_state))
            print("HUMAN MOTION DETECTED")
            if current_state:  # new
                #cam.start_preview()
                if INC==10:
                    INC=0
                INC +=1
                PATH='/home/pi/myvid/record'+str(INC)+'.h264'
                print("RECORDING STARTED")    
                print('Please Wait...')
                camera.start_recording(PATH)
                time.sleep(10)
                camera.stop_recording()
                print('Video recorded successfully')
                time.sleep(2)
                
                
        else:
            previous_state = current_state
            print("NO MOTION DETECCTED")
        
        


               
                
  





