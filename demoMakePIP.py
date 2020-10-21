"""
Demonstrates "picture-in-picture"
Submitted by: Christobel Nweke
"""

import lab7Functions
import cImage

myImage = cImage.FileImage("eiu.png")
billy = cImage.FileImage("billy.png")

# Upper left corner
newImage = lab7Functions.makePIP(myImage, billy, 0, 0)

# Upper right corner
newImage = lab7Functions.makePIP(newImage,
                                 billy,
                                 0,
                                 newImage.getWidth() - billy.getWidth())

# Lower left corner
newImage = lab7Functions.makePIP(newImage,
                                 billy,
                                 newImage.getHeight() - billy.getHeight(),
                                 0)

# Lower right corner
newImage = lab7Functions.makePIP(newImage,
                                 billy,
                                 newImage.getHeight() - billy.getHeight(),
                                 newImage.getWidth() - billy.getWidth())

lab7Functions.displayImage(newImage)
