"""
Demonstrates displayImage function

Submitted by: Christobel Nweke
"""

import lab7Functions
import cImage

# Desired size of the rectangular image
width = 700
height = 600

# Create a square image of a single color, initially black
amazingImage = cImage.EmptyImage(width, height)

# Change every pixel in this square to blue
for row in range(height):
    for col in range(width):
        amazingImage.setPixel(col, row, lab7Functions.magentaPixel)

# ... and display it
lab7Functions.displayImage(amazingImage)

