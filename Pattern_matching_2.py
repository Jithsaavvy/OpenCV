#Simple program to implement template matching

import cv2 
import numpy as np 
   
img_read = cv2.imread('sampleimg.png'). 
img_gray = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY) 
template = cv2.imread('template',0) 
w, h = template.shape[::-1] 
  
#Using matchTemplate() 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
threshold = 0.8
loc = np.where( res >= threshold)  
  
# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
  
# Show the final image with the matched area. 
cv2.imshow('Detected',img_rgb) 



//Reference: https://docs.opencv.org