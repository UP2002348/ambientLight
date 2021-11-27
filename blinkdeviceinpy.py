import pyfirmata
import getcolour

board = pyfirmata.Arduino('COM5')

#defines the pins that are connected to the board with the pwm as output method
blue = board.get_pin('d:3:p')
green = board.get_pin('d:5:p')
red = board.get_pin('d:6:p')

blueValue = 0
greenValue = 0
redValue = 0

blue.write(blueValue)
green.write(greenValue)
red.write(redValue)

while True:
    rgbValues = getcolour.colour()
    
    blueValue = rgbValues[2]
    greenValue = rgbValues[1]
    redValue = rgbValues[0]
    
    red.write(redValue)
    green.write(greenValue)
    blue.write(blueValue)

