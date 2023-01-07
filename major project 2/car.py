import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('haarcascade_car.xml') #the xml file has the information regarding the various patterns of cars 

cap = cv2.VideoCapture("cars.mp4") #reading the video

while cap.isOpened(): #the loop'll go on untill the video ends
    ret, img = cap.read() #reading the images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to gray image
    cars = car_cascade.detectMultiScale(gray, 1.3, 5) #calling car_cascade and defining the size of window , the scale factor is 1.3 and there are atleast 2 naighbouring objects in one frame

    for (x,y,w,h) in cars: #the quordinats and size of the cars are in x y w h
        cv2.rectangle(img,(x,y),(x+w+5,y+h+5),(0,0,255),3) #based on the quordinats and size the red rectangles are drawn

    cv2.imshow('Car Detector',img) #displaying the image with rectangles
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
