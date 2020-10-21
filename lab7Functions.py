"""
MAT 2170
Support functions for Lab 7

Submitted by: Christobel Nweke
"""

import cImage
import math

# Some common colors
redPixel = cImage.Pixel(255, 0, 0)
greenPixel = cImage.Pixel(0, 255, 0)
bluePixel = cImage.Pixel(0, 0, 255)
magentaPixel = cImage.Pixel(255, 0, 255)
yellowPixel = cImage.Pixel(255, 255, 0)
cyanPixel = cImage.Pixel(0, 255, 255)
whitePixel = cImage.Pixel(255, 255, 255)
blackPixel = cImage.Pixel(0, 0, 0)


def displayImage(image):
    """
    Display an image in an appropriately sized window

    Arguments:
        image: a graphics image

    Returns:
        None
    """
    # Create a window of the correct dimensions
    width = image.getWidth()
    height = image.getHeight()
    imageWindow = cImage.ImageWin("Image Viewer", width, height)

    # Display the image in this window
    image.draw(imageWindow)

    # Wait for a mouse click to close the window
    imageWindow.exitOnClick()


def makeDiagonal(size, desiredPixel):
    """
    Create an image with dimensions (size x size) of a given pixel in the
    shape of a diagonal line from the northwest to southeast corners.

    Arguments:
        size: width and height, in pixels, of image to be generated
        desiredPixel: color of diagonal line (background will be black)

    Returns:
        a square image with the specified properties
    """
    # Begin with a square image with all black pixels
    resultImage = cImage.EmptyImage(size, size)

    # Set pixels along the diagonal

    for i in range(size):
        resultImage.setPixel(i, i, desiredPixel)
    return resultImage


def makeRectangle(width, height, desiredPixel):
    """
    Create a rectangular image of specified size and color

    Arguments:
        width: desired width, in pixels, of rectangle
        height: desired height, in pixels, of rectangle
        desiredPixel: color for each pixel in the rectangle

    Returns:
        a rectangle with the specified properties
    """
    resultImage = cImage.EmptyImage(width + 100, height + 100)

    for col in range(height):
        for row in range(width):
         resultImage.setPixel(row,col,desiredPixel)

    return resultImage


def makeLowerTriangle(size, desiredPixel):
    """
    Create an image with dimensions (size x size) of a given pixel in the
    shape of a lower triangle

    Arguments:
        size: width and height, in pixels, of image to be generated
        desiredPixel: desired color of pixels in the lower triangle
                      (remaining pixels are black)

    Returns:
        a square image with the specified properties
    """
    # Begin with a square image with all black pixels
    resultImage = cImage.EmptyImage(size, size)
    for col in range(size):
        for row in range(size):
            resultImage.setPixel(col,row,blackPixel)

    for col in range(size):
        for row in range(col):
            resultImage.setPixel(row,col,desiredPixel)

    return resultImage

def makeBandedDiagonal(size, bandWidth, desiredPixel):
    """
    Create a banded diagonal image of (size x size) overall size, using the
    given pixel to highlight this band

    Arguments:
        size: width and height, in pixels, of image to be generated
        bandWidth: number of super-diagonals (and sub-diagonals) to appear
        desiredPixel: desired color of band

    Returns:
        a square image with the specified properties
    """
    resultImage = cImage.EmptyImage(size, size)
    for col in range(size):
        for row in range(size):
            resultImage.setPixel(col, row, blackPixel)
            resultImage.setPixel(col, col, desiredPixel)

    for i in range(size):
        for j in range(bandWidth):
            if i+j < size:
                resultImage.setPixel(i+j, j, blackPixel)
                resultImage.setPixel(i, i+j, desiredPixel)

    return resultImage


def displayImageFile(fileName):
    """
    Displays an image file in an appropriately sized window

    Arguments:
        fileName: the name of a file holding a graphics image (*.gif, *.png, etc.)

    Returns:
        None
    """
    # Get the image file
    theImage = cImage.FileImage(fileName)

    # Display it
    displayImage(theImage)


def makePIP(largeImage, smallImage, upperLeftRow, upperLeftCol):
    """
    Create an image of a "picture-in-picture"

    Arguments:
        largeImage: a graphics image
        smallImage: a smaller image to be placed within the larger image
        upperLeftRow: how far down to place the smaller image
        upperLeftCol: how far over to place the smaller image

    Returns:
        The image with the small image placed within the large image. The upper
        left corner of this small image appears at the given row and column.
    """
    # Start with an empty image large enough to hold the result
    resultImage = cImage.EmptyImage(largeImage.getWidth(), largeImage.getHeight())
    #copyLimage = cImage.FileImage(largeImage)

    # Make a copy of the large image
    heightl = largeImage.getHeight()
    widthl = largeImage.getWidth()
    for i in range(widthl):
        for j in range(heightl):
            lpixel = largeImage.getPixel(i, j)
            resultImage.setPixel(i, j, lpixel)

    # Place the smaller image within the larger one
    height2 = smallImage.getHeight()
    width2 = smallImage.getWidth()
    for i in range(width2):
        for j in range(height2):
            sPixel = smallImage.getPixel(i,j)
            resultImage.setPixel(i + upperLeftCol, j + upperLeftRow, sPixel)


    return resultImage


def displayFramedImage(image, frameSize, frameColor):
    """
    Display an image with a border of a specified color

    Arguments:
        image: a graphics image
        frameSize: desired size, in pixels, of the outer frame
        frameColor: desired color of frame

    Returns:
        None
    """
    width = image.getWidth()
    height = image.getHeight()
    resultImage = cImage.EmptyImage(width + 2 * frameSize, height + 2 * frameSize)

    # Create a frame(or a rectangle)
    for i in range(width+2*frameSize):
        for j in range(height+2*frameSize):
            resultImage.setPixel(i,j,frameColor)

    # Place image on center of frame
    for i in range(width):
        for j in range(height):
            pixel = image.getPixel(i,j)
            resultImage.setPixel(i+frameSize,j+frameSize,pixel)


    return displayImage(resultImage)


def makeStackedImages(topImage, bottomImage):
    """
    Given two images, produce a stacked version, one atop another

    Arguments:
        topImage: a graphics image
        bottomImage: a second graphics image

    Returns:
        The graphics image formed by stacking the two images
    """
    twidth = topImage.getWidth()
    theight = topImage.getHeight()
    bwidth = bottomImage.getWidth()
    bheight = bottomImage.getHeight()
    height = theight + bheight
    if twidth < bwidth:
        width = bwidth
    else:
        width = twidth
    resultImage = cImage.EmptyImage(width, height)
    for i in range(twidth):
        for j in range(theight):
            tpixel = topImage.getPixel(i, j)
            resultImage.setPixel(i, j, tpixel)

    for i in range(bwidth):
        for j in range(bheight):
            bpixel = bottomImage.getPixel(i, j)
            resultImage.setPixel(i, j + theight, bpixel)

    return resultImage


def pixelMapper(image, rgbFunction):
    """
    Apply a pixel-based function to every pixel of an image

    Arguments:
        image: an image to process
        rgbFunction: a function which can be applied to one pixel

    Returns:
        The image, with the supplied function applied to each pixel
    """

    # Create an image of the same size as the input image
    width = image.getWidth()
    height = image.getHeight()
    resultImage = cImage.EmptyImage(width, height)

    # Apply the given pixel function to each of the pixels in the image
    for row in range(height):
        for col in range(width):
            originalPixel = image.getPixel(col, row)
            newPixel = rgbFunction(originalPixel)
            resultImage.setPixel(col, row, newPixel)

    return resultImage


def grayPixel(pixel):
    """
    Convert a given pixel to its gray scale equivalent value

    Arguments:
        pixel: one pixel

    Returns:
        The gray scale equivalent pixel
    """

    # Compute the average RGB intensity
    intensitySum = pixel.getRed() + pixel.getGreen() + pixel.getBlue()
    avgRGB = intensitySum//3

    # Create and return a new pixel with this average value for each component
    newPixel = cImage.Pixel(avgRGB, avgRGB, avgRGB)
    return newPixel


def flip(value):
    """
    Color reverse an RGB value

    Arguments:
        value: a color intensity

    Returns:
        The color-reversed intensity
    """
    return 255 - value


def negativePixel(oldPixel):
    """
    Invert a single pixel

    Arguments:
        oldPixel: one pixel of a graphics image

    Returns:
        The photographic negative of this pixel
    """
    # invert all three RGB values
    newRed = flip(oldPixel.getRed())
    newGreen = flip(oldPixel.getGreen())
    newBlue = flip(oldPixel.getBlue())

    # return a new pixel with these inverted values
    newPixel = cImage.Pixel(newRed, newGreen, newBlue)
    return newPixel


def sepiaPixel(oldPixel):
    """
    Convert a given pixel to its sepia equivalent value

    Arguments:
        oldPixel: one pixel of a graphics image

    Returns:
        The sepia tone version of the given pixel

    """
    r = oldPixel.getRed()
    g = oldPixel.getGreen()
    b = oldPixel.getBlue()

    newRed = 0.393 * r + 0.769 * g + 0.189 * b
    newGreen = 0.349 * r + 0.686 * g + 0.168 * b
    newBlue = 0.272 * r + 0.534 * g + 0.131 * b
    if newRed > 255:
        newRed = 255
    if newGreen > 255:
        newGreen = 255
    if newBlue > 255:
        newBlue = 255
    newPixel = cImage.Pixel(int(newRed), int(newGreen), int(newBlue))
    return newPixel



