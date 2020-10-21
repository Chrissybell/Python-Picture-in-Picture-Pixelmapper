"""
Demonstrates the makeStackedImages function
Submitted by: Christobel Nweke
"""

import lab7Functions
import cImage

# Read two files of photos
topImage = cImage.FileImage("flowers.png")
bottomImage = cImage.FileImage("tug.png")

# Create a stacked image with one photo above another, then display it
desiredImage = lab7Functions.makeStackedImages(topImage, bottomImage)
lab7Functions.displayImage(desiredImage)
