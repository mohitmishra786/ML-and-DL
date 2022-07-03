import cv2
import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\mohit\OneDrive\Desktop\My-Machine-Learning-And-Deep-Learning-Work\Modelling\OpenCV\images\download.jfif')
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

## Dilating Images, it will make the edges more dark and bold
dilated = cv.dilate(canny , (7,7) , iterations=3)
cv.imshow('Dilated' , dilated)


## Eroding the images, simply means turning back dilated image into canny, but it will not be exact same
eroded = cv.erode(dilated , (7,7) , iterations=3)
cv.imshow('Erodede' , eroded)

## Resizing
resized = cv.resize(img , (500 , 500) , interpolation= cv.INTER_CUBIC)
cv.imshow("Resized" , resized)

## Cropping
cropped = img[50:200 , 200:300]
cv.imshow('Cropped' , cropped)

cv.waitKey(0)