import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

"""
This script is an exercise to implement the histogram of an image.
"""

#print(cv.__version__)

# Read the classical FSM photo
img = cv.imread("flyingspaghettimonster.jpg")
grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Check if the image was read
if img is None:
    # Terminate program
    sys.exit("Could not read the image.")

# Calculate histogram 
histOriginal = np.array([])
# Define a BGR image space
color = ('b', 'g', 'r')


# Plot BGR histogram
for i,col in enumerate(color):
    # Calculate channel (B,G,R) histogram 
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    # Add a plot for each channel
    plt.plot(hist, color=col)
    # Limit the visible xXrange
    plt.xlim([0,256])
    # Save the histogram results in an array for the BRG channels if required
    np.append(histOriginal,hist)    
plt.title("Original image histogram")
plt.show()
# Close manually the histogram plot

# To calculate a grayscale image histogram 
plt.hist(grey.ravel(),256,[0,256])
plt.title("Grayscale image histogram")
plt.xlim([0,256])
# Close manually the histogram plot
plt.show()

cv.imshow("Original",img)
cv.imshow("Grayscale",grey)

cv.waitKey(0)

