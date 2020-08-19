import cv2
import numpy as np
import  matplotlib.pyplot as plt

def dimensions(img):
        heigth, width, channels = img.shape
        return heigth, width, heigth * width

def spectre(img, lowerBound, upperBound):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerBound, upperBound)
        return  cv2.bitwise_and(img, img, mask = mask)

def percent(img, color_spectre):
        height, width, area = dimensions(img)
        gray = cv2.cvtColor(color_spectre, cv2.COLOR_BGR2GRAY)
        return np.count_nonzero(gray) / area * 100
    
image_bgr = cv2.imread('picture.jpg')
height, width, area = dimensions(image_bgr)
                      
lowerRed = np.array([0,100,100])
upperRed = np.array([15, 255, 255])
lowerGray = np.array([100,0,75])
upperGray = np.array([125, 70, 230])
lowerBlack = np.array([125,11,10])
upperBlack = np.array([165, 255, 102])
lowerDarkGray = np.array([0,26,30])
upperDarkGray = np.array([30, 100, 120])
lowerWhite = np.array([5,26,140])
upperWhite = np.array([30, 70, 203])

print('Height =' ,height, 'px')
print('Width =' ,width, 'px')
print('Area =', area, 'px^2')
print('Red =', "%.2f" % percent(image_bgr, spectre(image_bgr, lowerRed, upperRed)), '%')
print('Gray =', "%.2f" % percent(image_bgr, spectre(image_bgr, lowerGray, upperGray)), '%')
print('Black =', "%.2f" % percent(image_bgr, spectre(image_bgr, lowerBlack, upperBlack)), '%')
print('Dark Gray =', "%.2f" % percent(image_bgr, spectre(image_bgr, lowerDarkGray, upperDarkGray)), '%')
print('White =', "%.2f" % percent(image_bgr, spectre(image_bgr, lowerWhite, upperWhite)), '%')

cv2.imshow('Original', image_bgr)
cv2.imshow('Red', spectre(image_bgr, lowerRed, upperRed))
cv2.imshow('Gray', spectre(image_bgr, lowerGray, upperGray))
cv2.imshow('Black', spectre(image_bgr, lowerBlack, upperBlack))
cv2.imshow('Dark Gray', spectre(image_bgr, lowerDarkGray, upperDarkGray))
cv2.imshow('White', spectre(image_bgr, lowerWhite, upperWhite))

cv2.waitKey(0)
cv2.destroyAllWindows()
