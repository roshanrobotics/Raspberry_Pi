Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: /home/pi/test1.py =========================
start while true
Please Wait...
Video recorded successfully
1st video done
start while true
Please Wait...

Traceback (most recent call last):
  File "/home/pi/test1.py", line 29, in <module>
    record_video(PATH)
  File "/home/pi/test1.py", line 11, in record_video
    camera.start_recording(PAT)
  File "/usr/lib/python2.7/dist-packages/picamera/camera.py", line 1043, in start_recording
    camera_port, output_port = self._get_ports(True, splitter_port)
  File "/usr/lib/python2.7/dist-packages/picamera/camera.py", line 559, in _get_ports
    self._check_camera_open()
  File "/usr/lib/python2.7/dist-packages/picamera/camera.py", line 538, in _check_camera_open
    raise exc
PiCameraRuntimeError: No data recevied from sensor. Check all connections, including the SUNNY chip on the camera board
>>> 
