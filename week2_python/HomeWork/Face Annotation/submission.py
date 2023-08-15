import cv2
import math
import matplotlib
import matplotlib.pyplot as plt

# Lists to store the points
start=[]
corner=[]

def drawBox(action, x, y, flags, userdata):
  # Referencing global variables 
  global start, corner
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    start=[(x,y)]
    # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    corner=[(x,y)]

    # Draw the Rectangle
    cv2.rectangle(source, (start[0]),(corner[0]), (0,255,0),1)
    cv2.imshow("Window",source)
    crop=source[start[0][1]+1:corner[0][1],start[0][0]+1:corner[0][0]]
    test=plt.imshow(crop[:,:,::-1])
    cv2.imwrite('face.jpg',crop)

source = cv2.imread("sample.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawBox)
k = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", source)
    cv2.putText(source,'''Choose start,and drag, ESC-exit/c-clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
              0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF

    # Another way of cloning
    if k==99:
        source= dummy.copy()
    




cv2.destroyAllWindows()