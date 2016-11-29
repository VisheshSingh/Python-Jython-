# Functions that Manipulate Pixels in a Picture
# Author: Vishesh Thakur
# 10/4/15

# Reduce the amount of red in a picture by 50%
def decreaseRed (picture) :
  for pix in getPixels(picture) :
    value = getRed(pix)
    setRed (pix, value * 0.5)
    
# Increase the amount of red in a picture by 20%
def increaseRed(picture) :
  for pix in getPixels(picture) :
    value = getRed(pix)
    setRed (pix, value * 1.2)

# Both functions have a picture parameter, 
# use a for loop to get each pixel in the picture, get the value of the red 
# channel for that pixel, and then change the value of that channel

# Yhe only difference is that increaseRed 
# multiplies the value of the red channel by a number greater than 1 and 
# decreaseRed multiplies the value of the red channel by a number less than 1


#changeRed: changes the value of the red channel by a specified factor
#The function has two parameters:  a picture and a factor which is a floating-point 
#number. If factor is greater than 1 the function increases the value of the red 
#channel in each pixel. If factor is less than 1 the function decreases the red
#channel in each pixel
#Examples of use: changeRed(myPic, 1.2)  changeRed(myPic, 0.6)
def changeRed(picture, factor) :
  for pix in getPixels(picture) :
    value = getRed(pix)
    setRed (pix, value * factor)

#changeBlue: changes the value of the blue channel by a specified factor
#the function has two parameters:  a picture, factor, a floating-point 
#number. If factor is greater than 1 the function increases the value of
#the blue channel in each pixel.  If factor is less than 1 the function
#decreases the blue channel in each pixel
#Examples of use: changeBlue(myPic, 1.2)  changeBlue(myPic, 0.6)
def changeBlue(picture, factor) :
  for pix in getPixels(picture) :
    value = getBlue(pix)
    setBlue (pix, value * factor)

#changeGreen: changes the value of the green channel by a specified factor
#the function has two parameters:  a picture, factor, a floating-point 
#number. If factor is greater than 1 the function increases the value of
#the green channel in each pixel.  If factor is less than 1 the function
#decreases the green channel in each pixel
#Examples of use: changeGreen(myPic, 1.2)  changeGreen(myPic, 0.6)
def changeGreen(picture, factor) :
  for pix in getPixels(picture) :
    value = getGreen(pix)
    setGreen (pix, value * factor)
    

#makeSunset(picture): this function simulates a sunset by decreasing the
#values of blue and green channels in each pixel of a picture
def makeSunset (picture) :
  changeBlue (picture, 0.7)
  changeGreen (picture, 0.7)


#mysteryEffect: sets the blue and green values for each pixel to the
#same value as the red channel
def mysteryEffect (picture) :
  for pix in getPixels (picture) :
    redValue = getRed(pix)
    setGreen (pix, redValue)
    setBlue (pix, redValue)
  
#Effect of this function on a picture: now the picture is a grayscale.  
#The red, green and blue channels of each pixel have the same value (the value of the red channel) 
#and so this creates a grayscale effect.


#mirrorHalf: 
#Mirrors the top half of the picture onto the bottom half of the picture
def mirrorHalf (picture) :
  pixels = getPixels(picture)
  target = len(pixels) - 1
  for index in range (0, len(pixels)/2 ) :
   pixel1 = pixels[index]
   color1 = getColor(pixel1)
   pixel2 = pixels[target]
   setColor(pixel2, color1)
   target = target - 1

#mirrorUpHalf: mirrors the bottom half of the picture into the top
def mirrorUpHalf (picture) :
  pixels = getPixels(picture)
  target = len(pixels) - 1
  for index in range (0, len(pixels)/2 ) :
   pixel1 = pixels[target]
   color1 = getColor(pixel1)
   pixel2 = pixels[index]
   setColor(pixel2, color1)
   target = target - 1