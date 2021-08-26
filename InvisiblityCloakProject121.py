import cv2
import time
import numpy as np

#to save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#start the webcam 
cap = cv2.VideoCapture(0)

#allowing the webcam to start by making the code sleep for two seconds
time.sleep(2)
bg = 0

#capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()

#flipping the background
bg = np.flip(bg, axis = 1)

#read the captured frame until the camera is on
while(cap.isOpened()):
    ret, frame = cap.read() 
    if not ret:
        break
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("Magic", f) 
    #cv2.imshow("mask", f) 

cap.release()
#out.release()
cv2.destroyAllWindows()