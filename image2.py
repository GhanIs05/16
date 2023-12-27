import cv2
import numpy as np
# Load the image
image_path = 'image.jpg' # Replace with the path to your image
image = cv2.imread(image_path)
# Display the original image
cv2.imshow('Image Display', image)
# Negation of the image (invert colors)
negated_image = cv2.bitwise_not(image)
cv2.imshow('Negated Image', negated_image)
# Rotation of the image (90 degrees clockwise)
rotation_angle = 90
rows, cols, _ = image.shape
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotation_angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
cv2.imshow('Rotated Image', rotated_image)
# Shrinking the image
shrink_scale = 0.5
shrunken_image = cv2.resize(image, None, fx=shrink_scale, fy=shrink_scale)
cv2.imshow('Shrunken Image', shrunken_image)
# Reversing the image (horizontal flip)
reversed_image = cv2.flip(image, 1)
cv2.imshow('Reversed Image', reversed_image)
# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
