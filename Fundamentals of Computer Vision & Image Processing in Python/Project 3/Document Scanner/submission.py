import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('scanned-form.jpg')

imageGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

grayblur=cv2.GaussianBlur(imageGray,(5,5),0)
canny=cv2.Canny(grayblur,30,50)

contours, heirarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv2.contourArea,reverse=True)

for c in contours:
    epi= 0.02*cv2.arcLength(c,True)
    corners=cv2.approxPolyDP(c,epi,True)
    if len(corners)==4:
        target=corners
        break

out=image.copy()        
cv2.drawContours(out,[target],-1,[0,255,0],10)

output=[[0,0],[1000,0],[1000,1333],[0,1333]]

M=cv2.getPerspectiveTransform(np.float32(target),np.float32(output))

final=cv2.warpPerspective(image,M,(output[2][0],output[2][1]),flags=cv2.INTER_LINEAR)

warpedimage=cv2.flip(final,1)

cv2.imwrite('FinalScanned.jpg',warpedimage)



