import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\mohit\OneDrive\Desktop\OpenCV\images\download.jfif')
cv.imshow('Anime' , img)


## Converting into GrayScale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Anime' , gray)

## Making Images Blurred
blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow('Blurred' , blur)

## Finding Edges
canny = cv.Canny(img , 125 , 175)
cv.imshow('Canny' , canny)

# WE can reduce edges by using blurred images/ Making image blurred
canny = cv.Canny(blur , 125 , 175)
cv.imshow('Canny' , canny)




cv.waitKey(0)