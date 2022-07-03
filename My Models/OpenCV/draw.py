import cv2 as cv
import numpy as np

# Let's make blank image
blank = np.zeros((500, 500 , 3) , dtype='uint8')
cv.imshow('Blank Image' , blank)


# Coloring some portion 

# blank[200:300 , 300:400] = 0, 255 , 0
# cv.imshow('Colored' , blank)


# making rectangle in image

# cv.rectangle(blank , (0,0) , (250,250) , (0 ,0 , 255) , thickness=2)
# cv.imshow('Rectangle' , blank)

# Filling the whole rectangle 
# Rather than using cv.FILLED we can also pass -1 into thickness and the Reactngle will be filled
cv.rectangle(blank , (250 , 250) , (500, 500) , (255, 0 , 0) , thickness= cv.FILLED)
cv.imshow('Filled Rectangle' , blank)


# Circle
cv.circle(blank, (blank.shape[1]//2 , blank.shape[0]//2) ,50 , (0 , 0 , 255) , thickness= 4)
cv.imshow('Circle' , blank)

# Draw a Line
cv.line(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0]//2) , (255 , 255, 255) , thickness=2)
cv.imshow('Line' , blank)


# Putting Text Over Image

cv.putText(blank , 'Hello, Mohit' , (225,225) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0 , 255 , 255) , thickness=2)
cv.imshow('Image with Text' , blank)

# Loaded Image

# img = cv.imread('images/download.jfif')
# cv.imshow('Downloaded Pic', img)  

cv.waitKey(0)