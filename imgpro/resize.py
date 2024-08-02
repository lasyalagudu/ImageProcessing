import cv2

# Relative or absolute path of the input image file
path = "chris.png"

# Reading image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Rotating the image by 180 degrees
imageRot = cv2.rotate(image, cv2.ROTATE_180)

# Displaying the original and rotated images in separate windows
cv2.imshow("Output", image)
cv2.imshow("Rotated", imageRot)

# Waiting until any key press (press any key to close the window)
cv2.waitKey(0)

# Closing all the windows
cv2.destroyAllWindows()