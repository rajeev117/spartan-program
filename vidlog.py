import cv2
import numpy as np
import pyautogui as pgi
from PIL import ImageGrab
import time
'''#cam=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
filename="output"+str(time.time())+".avi"
out=cv2.VideoWriter(filename,fourcc,15.0,(1366,768))
time.sleep(3)
while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1)==37:
        break
out.release()
cv2.destroyAllWindows()

    #b,img=cam.read()
    cv2.imshow("ViewPort",img)
    rec.write(img)
    key=cv2.waitKey(1)&0xFF
    if key == ord('q'):
        rec.release()
        break
cam.release()
cv2.destroyAllWindows()
'''

cc=cv2.VideoWriter_fourcc(*"XVID")
screen=pgi.size()
filename="output"+str(time.time())+".mp4"
output=cv2.VideoWriter(r"E:\Rajeev\vidlog.avi",cc,20.0,screen)
time.sleep(3)
while True:
    img=ImageGrab.grab()
    img=pgi.screenshot()
    frames=np.array(img)
    frames=cv2.cvtColor(frames,cv2.COLOR_BGR2RGB)
    output.write(frames)
    cv2.imshow("REcording",frames)
    if cv2.waitKey(1)==ord("q"):
        break
cv2.destroyAllWindows()
output.release()
 #import mysql-connector as msc
 #host