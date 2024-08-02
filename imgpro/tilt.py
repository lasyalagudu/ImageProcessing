import cv2

# Relative or absolute path of the input image file
path = "test.png"

# Reading image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Get the size of the image
size = image.shape
height = size[0]
width = size[1]

# Define the center of the image
center = (int(width / 2), int(height / 2))

# Get the rotation matrix for rotating the image by 45 degrees around the center
M = cv2.getRotationMatrix2D(center, 45, 1)

# Perform the rotation
imageRot = cv2.warpAffine(image, M, (width, height))

# Display the original image in a window
cv2.imshow("Output", image)

# Display the rotated image in a window
cv2.imshow("Rotate", imageRot)

# Wait until any key press (press any key to close the window)
cv2.waitKey(0)

# Kill all the windows
cv2.destroyAllWindows()
