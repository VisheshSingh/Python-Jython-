#  Functions that return values, and nested for loops
# Author: Vishesh Thakur
# October 17, 2015

#Vertical Reflection function creates a vertical reflection of a picture. It
#takes a picture as a parameter, and returns a new picture of the same size reflected
#vertically around the right edge.
def verticalReflection (picture):
  w = getWidth(picture)
  h = getHeight(picture)
  canvas = makeEmptyPicture(w, h)
  targetX = getWidth(canvas) - 1
  for sourceX in range (0, getWidth(picture)) :
    targetY = 0
    for sourceY in range (0, getHeight(picture)) :
      color = getColor(getPixel(picture, sourceX, sourceY))
      setColor (getPixel(canvas, targetX, targetY), color)
      targetY = targetY + 1
    targetX = targetX - 1
  return (canvas)


#MirrorVertical works with half of the source picture and copies the 
#left half of the source picture onto the canvas on the ride side and 
#then fills the right side of the target canvas with a reflection of the 
#left half of the source picture. verticalReflection takes the whole 
#source picture and copies each pixel of it into the target canvas but 
#on the opposite side (that is, a pixel from the left is copied into the right) 


#function to blend two pictures into one.  
#Improvements: added parameters to the function so it takes any two pictures
#to be blended and the desired amount of overlap (given in pixels)
def blendPictures(pic1, pic2, overlapAmount) :
  #set up 
  height =  max(getHeight(pic1), getHeight(pic2))
  canvas = makeEmptyPicture((getWidth(pic1) + getWidth(pic2) - overlapAmount) , height)
  
  pic1Width = getWidth(pic1)
  
  #copy first part of pic1 into the canvas
  #first part of pic1 = pict1Width - amount of overlap
  pixelsFromPic1 = getWidth(pic1) - overlapAmount
  sourceX = 0
  for targetX in range (0, pixelsFromPic1) :
    sourceY = 0
    for targetY in range (0, getHeight(pic1)) :
      color = getColor(getPixel(pic1, sourceX, sourceY))
      setColor (getPixel(canvas, targetX, targetY), color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
  
  #copy the overlap bw pic1 and pic2 into the canvas
  #make a new color for the overlap effect
  #taking 50% of each color channel from both pics
  minHeight =  min(getHeight(pic1), getHeight(pic2))
  sourceX = 0
  for targetX in range (pixelsFromPic1, pic1Width) :
    sourceY = 0 
    for targetY in range (0, minHeight) :
      pic1Pixel = getPixel(pic1, sourceX + pixelsFromPic1, sourceY)
      pic2Pixel = getPixel(pic2, sourceX, sourceY)
      newRed = 0.50 * getRed(pic1Pixel) + 0.50 * getRed(pic2Pixel)
      newGreen = 0.50 * getGreen(pic1Pixel) + 0.50 * getGreen(pic2Pixel)
      newBlue = 0.50 * getBlue(pic1Pixel) + 0.50 * getBlue(pic2Pixel)
      color = makeColor(newRed, newGreen, newBlue)
      setColor(getPixel(canvas, targetX, targetY), color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
    
  #now copy the second part of pic2 into the canvas
  #second part of pic2 starts at: overlapAmount
  sourceX = overlapAmount
  for targetX in range (pixelsFromPic1 + overlapAmount, getWidth(pic2) + pixelsFromPic1) :
    sourceY = 0
    for targetY in range (0, getHeight(pic2)) :
      color = getColor(getPixel(pic2, sourceX, sourceY))
      setColor(getPixel(canvas, targetX, targetY), color)
      sourceY = sourceY + 1
    sourceX = sourceX + 1
  
  #return the blended picture
  return canvas

#Draw the flag of Kazooistan.  
#  The flag is square with three colored regions: 
#  the upper left quadrant is black, the upper right quadrant is orange
#  and the bottom half is white.  
#Parameter: size -- the width and height of the flag.
#Returns: an image of the flag.
#HERE IS THE CORRECTED VERSION
def flag(size):
    pic = makeEmptyPicture(size, size)
    for x in range(size):
      for y in range(size):
        pix = getPixel(pic, x, y)
        # make the upper left black
        if y <= (.5 * size) and x <= (.5 * size):
          setColor(pix, black)
        # make the upper right orange
        if y <= (.5 * size) and x >= (.5 * size):
          setColor(pix, orange)
    return pic    

