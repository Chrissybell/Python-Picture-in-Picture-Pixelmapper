"""
Demonstrates the displayFramedImage function
"""
"Submitted by: Christobel Nweke"

import lab7Functions
import cImage

# Frame a photo with a narrow yellow frame
myImage = cImage.FileImage("flowers.png")
lab7Functions.displayFramedImage(myImage, 20, lab7Functions.yellowPixel)

# Frame some artwork with a magenta frame
tugImage = cImage.FileImage("tug.png")
lab7Functions.displayFramedImage(tugImage, 50, lab7Functions.magentaPixel)
