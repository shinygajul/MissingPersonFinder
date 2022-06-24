import faceRecCamera as cam
import faceRec as rec
import time
while(True):
    #x = input("Press Q to quit, Enter to continue: " )
    #if(x == 'Q'):
        #print("quitting")
       # break
    time.sleep(10)
    cam.takePicture()
    print("picture being taken")
    print("picture taken")
    print("starting facial rec")
    rec.runRec()
    print("facial rec done")
cam.stopCam()