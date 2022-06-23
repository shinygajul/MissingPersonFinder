#!//usr/bin/python3

from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.still_configuration(main={"size": (320, 240)})
picam2.configure(config)
picam2.start()

def takePicture():
    print("taking picture")
    np_array = picam2.capture_array()
    #print(np_array)
    #picam2.capture_file("demo.jpg")
    picam2.capture_file("unknown_faces/demo.jpg")
def stopCam():
    picam2.stop()
if __name__ == "__main__":
    takePicture()
    stopCam()
    
