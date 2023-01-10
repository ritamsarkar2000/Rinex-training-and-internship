import cv2
import numpy as np

size = 800     #board size in pixel
sqnum = 8      #8 squares per side,  so there will be 8x8 checker board
sqsize = int(800/8) #size of each squares in pixels

darkcolor = (0,0,0)        #black
lightcolor = (255,255,255) #white

currentcolor = darkcolor   #the color of the square to be painted currently

print("The checker board")

#creating the board
while True:
    x = np.zeros([size,size,3],dtype = np.uint8)
    for row in range(0,sqnum):
        for column in range(0,sqnum):
            x[sqsize*row:sqsize*(row+1), sqsize*column:sqsize*(column+1)] = currentcolor
            if currentcolor == darkcolor:
                currentcolor = lightcolor
            else:
                currentcolor = darkcolor
        if currentcolor == darkcolor:
            currentcolor = lightcolor
        else:
            currentcolor = darkcolor
    
    cv2.imshow("the board",x)
    if cv2.waitKey(1) & 0xff == ord('q'): #press q to stop
        break
    
