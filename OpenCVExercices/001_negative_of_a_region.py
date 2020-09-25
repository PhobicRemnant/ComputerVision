#%%
import cv2 as cv
import numpy as np
import sys

"""
This script is an exercise to implement the negative of an image.
"""


# Read the classical Lena photo
img = cv.imread("flyingspaghettimonster.jpg")

# Check if the image was read
if img is None:
    # Terminate program
    sys.exit("Could not read the image.")


# Get and show the image rows and columns 
size = img.shape 
print("The image is {} by {}".format(size[0], size[1]))

# Create two random points within the image size
pt1 = np.rint(np.random.rand(2)*size[0])
pt1.sort() # Needed to go from min to max
pt2 = np.around(np.random.rand(2)*size[1])
pt2.sort()

# Take a random section of the image
imgSubSection = img[ int(pt1[0]):int(pt1[1]), int(pt2[0]):int(pt2[1]),:]

# To invert the color of a pixel the used formula is "color = 255 - color"
for i in range( int(pt1[0]), int(pt1[1]) ):
    for j in range( int(pt2[0]), int(pt2[1]) ):
        img[i,j,0] = 255 - img[i,j,0]
        img[i,j,1] = 255 - img[i,j,1]
        img[i,j,2] = 255 - img[i,j,2]

# Display image in window
cv.imshow("He boiled for our sins.",img)
cv.waitKey() & 0xFF # The 0xFF is required only if you are using a 64bit system

# Destroy all the created windows 
cv.destroyAllWindows()


# %%
