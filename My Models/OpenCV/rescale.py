from turtle import width
import cv2 as cv
from cv2 import resize
from cv2 import INTER_AREA

# image = cv.imread('images/download.jfif')
# cv.imshow('Image' , image)

def rescaleFrame(frame , scale = 0.75):

    # Work for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

def changeRes(width , height):
    
    # Work for Live Videos Only
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('videos/kitten.mp4')
while True:
    isTrue , frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('videos' , frame)
    cv.imshow('videos' , frame_resized)


    if 0xFF==ord('d') & cv.waitKey(20):
        break

capture.release()
cv.destroyAllWindows()
