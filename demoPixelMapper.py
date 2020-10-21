"""
Demonstrates the pixelMapper function
Submitted by: Christobel Nweke
"""

import lab7Functions
import cImage

# Read an image to be transformed
oldImage = cImage.FileImage("flowers.png")

# Transform the image
newImageG = lab7Functions.pixelMapper(oldImage, lab7Functions.grayPixel)
newImageN = lab7Functions.pixelMapper(oldImage, lab7Functions.negativePixel)
newImageS = lab7Functions.pixelMapper(oldImage, lab7Functions.sepiaPixel)


lab7Functions.displayImage(lab7Functions.makeStackedImages(oldImage, newImageG))
lab7Functions.displayImage(lab7Functions.makeStackedImages(oldImage, newImageN))
lab7Functions.displayImage(lab7Functions.makeStackedImages(oldImage, newImageS))
