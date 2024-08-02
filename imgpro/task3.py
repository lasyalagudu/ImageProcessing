import cv2
import numpy as np

# Global variables shared between the mouseClick function and rest of the code
draw = False
reset = False

# Initially p1 and p2 = 0
p1 = (0, 0)
p2 = p1

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global draw, reset, p1, p2
    
    # If left click press event, enable drawing and set p1 and p2 as current position
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        reset = False
        p1 = (xPos, yPos)
        p2 = p1
    
    # Continuously update p2 on mouse movement and left mouse press
    elif event == cv2.EVENT_MOUSEMOVE and draw:
        p2 = (xPos, yPos)
    
    # If left click release, stop drawing
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
    
    # If right click, reset the frame/canvas, and p1 and p2 to 0
    elif event == cv2.EVENT_RBUTTONDOWN:
        reset = True
        p1 = (0, 0)
        p2 = p1

# Creating a black image/frame (0 pixel value) of 500x500 size
frame = np.zeros((500, 500, 3), np.uint8)

# Creating a window to display image/frame
cv2.namedWindow('FRAME')

# This function detects every new event and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    cv2.line(frame, p1, p2, (0, 255, 0), 2)
    
    # Swapping points for next line segment (p2 copies to p1 and p2 updates to latest position)
    p1 = p2
    
    cv2.imshow('FRAME', frame)
    
    if reset:
        # Renew black frame on right click
        frame = np.zeros((500, 500, 3), np.uint8)
    
    # To quit press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
