import RPi.GPIO as gpio 
from picamera import Picamera
import time
def record_video():
	print('Please Wait...')
	Picamera.start_preview()
	Picamera.start_recording('/home/pi/Desktop/rec.h264')
	time.sleep(5)
	
	Picamera.stop_recording()
	Picamera.stop_preview()
	print('Video recorded successfully')
	time.sleep(2)

print('1')
camera = picamera.PiCamera()
print('2')
camera.rotation=180
print('3')
camera.awb_mode= 'auto'
print('4')
camera.brightness=55
print('5')

while True:
    print('done')

    a=record_video()
    print('done')
