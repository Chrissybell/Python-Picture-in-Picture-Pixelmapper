"""
Demonstrates makeBandedDiagonal function

Submitted by: Christobel Nweke
"""

import lab7Functions


# Create an image and display it
amazingImage = lab7Functions.makeBandedDiagonal(400, 1, lab7Functions.redPixel)
lab7Functions.displayImage(amazingImage)

# Now a second image
amazingImage = lab7Functions.makeBandedDiagonal(400, 3, lab7Functions.greenPixel)
lab7Functions.displayImage(amazingImage)

# And a third
amazingImage = lab7Functions.makeBandedDiagonal(400, 100, lab7Functions.bluePixel)
lab7Functions.displayImage(amazingImage)
