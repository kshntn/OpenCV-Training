import cv2
import math

# Lists to store the points
leftpoint=[]
rightpoint=[]


def drawbox(action, x, y, flags, userdata):
  # Referencing global variables 
  global left, right
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    left=[(x,y)]
    # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    right=[(x,y)]
    # Draw the circle
    cv2.rectangle(source, left[0], right[0], (0, 255, 0), thickness=1, lineType=cv2.LINE_AA);
    cv2.imwrite("face.png",source[left[0][1]:right[0][1],left[0][0]:right[0][0]])
    cv2.imshow("Window",source)



source = cv2.imread("images/sample.jpg",1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawbox)
k = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", source)
    cv2.putText(source,'''Choose top left, and drag, 
                Press ESC to exit and c to clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
              0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k==99:
        source= dummy.copy()


cv2.destroyAllWindows()