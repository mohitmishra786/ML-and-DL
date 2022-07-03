import cv2 as cv

# Image Reader

# anime = cv.imread('images/download (1).jfif')
# cv.imshow('Download' , anime)
# cv.waitKey(0)

# Video Reader

capture = cv.VideoCapture('videos/kitten.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('videos' , frame)

    if 0xFF==ord('d') & cv.waitKey(20):
        break

capture.release()
cv.destroyAllWindows()



