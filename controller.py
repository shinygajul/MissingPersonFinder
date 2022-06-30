import faceRecCamera as cam
import faceRec as rec
import time
while(True):
    time.sleep(2)
    cam.takePicture()
    print("picture being taken")
    print("picture taken")
    print("starting facial rec")
    rec.runRec()
    print("facial rec done")
cam.stopCam()