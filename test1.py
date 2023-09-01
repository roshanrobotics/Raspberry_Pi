import RPi.GPIO as GPIO
import picamera 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
INC=0
def record_video(PAT):
	print('Please Wait...')
	
	camera.start_recording(PAT)
	time.sleep(5)

	camera.stop_recording()

	print('Video recorded successfully')
	time.sleep(2)
		


camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
		   
while True:
    PATH='/home/pi/myvid/rec'+str(INC)+'.h264'
    print("start while true")
    record_video(PATH)
    time.sleep(1)
    print("1st video done")
    INC +=1
    if INC==10:
            INC=0
            
