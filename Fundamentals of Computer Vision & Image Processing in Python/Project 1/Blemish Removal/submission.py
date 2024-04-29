import numpy as np
import cv2 as cv

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv.imshow(self.windowname, self.dests[0])
#         cv.imshow(self.windowname + ": mask", self.dests[1])

    def on_mouse(self,event,x,y,flags,param):
        pt = (x, y)
        if event == cv.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv.circle(dst,pt,10,(255,0,0),-1)
                res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=10, flags=cv.INPAINT_TELEA)
                cv.imshow('Inpaint Output', res)
                mouseX,mouseY=x,y

filename = "blemish.png"
img = cv.imread(filename, cv.IMREAD_COLOR)

if img is None:
    print('Failed to load image file: {}'.format(filename))

img_mask = img.copy()
inpaintMask = np.zeros(img.shape[:2], np.uint8)
print("Radius of 10 used for inpainting. Press Esc for exit")

sketch = Sketcher('image', [img_mask, inpaintMask], lambda : ((0, 255, 255), 255))


while(1):
    cv.imshow('image',img)
    k=cv.waitKey(20) & 0xFF
    if k==27:
        break
