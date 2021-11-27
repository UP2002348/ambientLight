import PIL.ImageGrab as ig
from statistics import mode

def mostCommon(rgbli):
    return(mode(rgbli))

def convertRGBColour(RGBcolour):
    redValue = RGBcolour[0] / 255

    greenValue = RGBcolour[1] / 255
    
    blueValue = RGBcolour[2] / 255 
    

    return((redValue, greenValue, blueValue))

def colour():
    rgblist = []
    image = ig.grab()

    for y in range(0, 1080, 10):
        for x in range(0, 1920, 10):
            color = image.getpixel((x, y))
            rgblist.append(color)

    newColour = convertRGBColour(mostCommon(rgblist))
    return(newColour)
