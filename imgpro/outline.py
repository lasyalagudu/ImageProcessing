# Importing OpenCV Library
import cv2

# Relative or absolute path of the input image file
path = "test.png"

# Reading image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Detecting edges using Canny edge detector
edges = cv2.Canny(image, 200, 300)

# Display image in a window
cv2.imshow("Output", image)
cv2.imshow("Edges", edges)

# Wait until any key press (press any key to close the window)
cv2.waitKey(0)

# Kill all the windows
cv2.destroyAllWindows()
