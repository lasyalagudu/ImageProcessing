# import cv2 
# # Relative or absolute path of the input image file 
# path =  "chris.png" 
# # reading image (by default the flag is 1 if not specidied) 
# image = cv2.imread(path) 
# image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
# # Display image in a window 
# cv2.imshow(image)
# cv2.imshow(image_gray) 
# # Wait until any key press (press any key to close the window) 
# cv2.waitKey() 
# # kill all the windows 
# cv2.destroyAllWindows()
import cv2

# Relative or absolute path of the input image file
path = "chris.png"

# Reading image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Converting image to Grayscale (also OpenCV reads image in BGR format and hence BGR to Gray)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display image in a window
cv2.imshow("Output", image)
cv2.imshow("Output_gray", image_gray)

# Wait until any key press (press any key to close the window)
cv2.waitKey(0)

# Kill all the windows
cv2.destroyAllWindows()
