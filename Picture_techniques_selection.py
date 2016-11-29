#    Picture Techniques with Selection
# Author: Vishesh Thakur
# October 9, 2015
   
# turnToGreen(): This function takes a photo as a parameter and modifies that photo so that
# every pixel that is "sufficiently the target color" is converted instead to a pixel that 
# is "sufficiently green"
# 20 POINTS  
def turnToGreen(picture, colorToChange, threshold) :
  for px in getPixels(picture) :
    pxColor = getColor(px)
    redValue = getRed(px)
    greenValue = getGreen(px)
    if ( distance(pxColor, colorToChange) < threshold ) :
      setRed(px, greenValue)
      setGreen(px, redValue)


#posterizeMe(picture): this function posterizes a picture
#according to the rules given in the lab instructions
# 30 POINTS for the functions
def posterizeMe (picture) :
  #loop through the picture and get each pixel's red, green and blue channels
  for p in getPixels(picture) :
    pRed = getRed(p)
    pGreen = getGreen(p)
    pBlue = getBlue(p)
    
    #implement the changes
    if (pRed > 80 and pRed <= 167) :
      setRed (p, pGreen)    
    elif (pRed >= 90) :
      setRed(p, 255)
    
    if (pBlue < 90) :
      newBlue = pRed
      newRed = pBlue
      setBlue(p, newBlue)
      setRed(p, newRed)     

    if (pGreen > 130) :
      setGreen (p, 130)
    else :   #pGreen <= 130
      newRed = abs (pBlue - pRed)
      setRed(p, newRed)
  
  #show resulting picture -- this line could be omitted
  repaint (picture)

# (a) A pure blue pixel will turn to magenta (255, 0, 255) and a 
#     pure red pixel will turn to magenta (255, 0, 255) as well.
# (b) It is important to store the original red, green and  blue values
#     before the if statements because the checks done by the if statements 
#     need the original values of the red, green, and blue channels.



#changeFace(): this function takes a picture with the face of a person and
#changes it by turning the teeth purple, the eyes red, and the hair orange
#parameters include: a picture with a person's face
#                    the X, Y coordinates of the upper-left and bottom-right of the teeth area
#                    the X, Y coordinates of the upper-left and bottom-right of the eye area
#                    the X, Y coordinates of the upper-left and bottom-right of the hair area
#                    the original teeth, eye, and hair colors
#                    teethDistance, eyeDistance, hairDistance are the thresholds use to decide if the color should be changed 

def changeFace (picture, teethStartX, teethStartY, teethEndX, teethEndY, teethColor, teethDistance, eyesStartX, eyesStartY, eyesEndX, eyesEndY, eyesColor, eyesDistance, hairStartX, hairStartY, hairEndX, hairEndY, hairColor, hairDistance):
  for px in getPixels(picture) :
    x = getX(px)
    y = getY(px)
    pxColor = getColor(px)
    
    #change the teeth
    if (teethStartX <= x and x <= teethEndX) and (teethStartY <= y and y <= teethEndY) :
      if (distance(teethColor, pxColor) < teethDistance) :
        purple = makeColor(255, 0, 255)
        setColor(px, purple)

    #change the eyes
    if (eyesStartX <= x and x <= eyesEndX) and (eyesStartY <= y and y <= eyesEndY) :
      if (distance(eyesColor, pxColor) < eyesDistance) :
        setColor(px, green)
    
    #change the hair
    if (hairStartX <= x and x <= hairEndX) and (hairStartY <= y and y <= hairEndY) :
      if (distance(hairColor, pxColor) < hairDistance) :
        setColor(px, blue)
    
