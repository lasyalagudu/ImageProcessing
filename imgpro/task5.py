import cv2
import numpy as np

# Initialize variables
cropping = False
start_point = ()
end_point = ()

def mouse_crop(event, x, y, flags, param):
    global start_point, end_point, cropping

    # If left mouse button is clicked, record the starting point
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        cropping = True

    # If left mouse button is released, record the ending point and crop the image
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        cropping = False

        # Draw the rectangle on the image
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("image", image)

        # Crop the image
        if start_point != end_point:
            cropped_image = orig_image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
            cv2.imshow("cropped", cropped_image)
            cv2.imwrite("cropped_image.png", cropped_image)

# Read the image
image_path = "chris.png"  # Replace with your image path
image = cv2.imread(image_path)
orig_image = image.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

# Display the image and wait for a key press
while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # Exit the loop when 'q' is pressed
    if key == ord("q"):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
