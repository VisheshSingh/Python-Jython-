# Experimenting further with Sounds
# Author: VIshesh Thakur
# February 19, 2016

from soundUtilities import *  #this line will be added right before working with Append Sounds 
 
#Blend two sounds: this function blends 2 sounds: sound1 and sound2 at a
#given amount of overlap. overlapAmt is given in samples 
def blendSounds(sound1, sound2, overlapAmt):
  # Get the lengths (# of samples) in each sound
  length1 =  getLength(sound1)
  length2 =  getLength(sound2)

  # Make an empty sound large enough to hold the new sound
  totalNumSamples = length1 + length2 - overlapAmt
  newSound = makeEmptySound(totalNumSamples)

  # Copy first sound up to the overlap section
  firstPartEnd = length1 - overlapAmt
  for index in range (0, firstPartEnd) :
    value = getSampleValueAt(sound1, index)
    setSampleValueAt(newSound, index, value)

  # Add the overlap section 
  for index in range(0 , overlapAmt ):
    value1 =  getSampleValueAt(sound1, index + firstPartEnd)
    value2 =  getSampleValueAt(sound2, index)
    newValue = value1 * 0.5 + value2 * 0.5
    setSampleValueAt(newSound, index + firstPartEnd, newValue)

  # Copy the rest of sound2
  for index in range (overlapAmt, length2) :
    value = getSampleValueAt(sound2, index)
    setSampleValueAt(newSound, index + firstPartEnd, value)
 
  # return the new sound
  return newSound

  
#Appending sounds: apends sound2 at the end of sound1
#the solution for this problem MUST use the copy function given in soundUtilities.py
def appendSounds (sound1, sound2) :
  # Make an empty sound long enough to contain both source sounds.
  len = getLength(sound1) + getLength(sound2)
  newSound = makeEmptySound(len)

  # Copy sound1 into the beginning of the new sound
  #using copy (source, target, start) from soundUtilities.py
  copy(sound1, newSound, 0)
  
  # Copy sound2 into the end of the new sound 
  len1 = getLength(sound1) 
  copy(sound2, newSound, len1)

  # Return the new sound. 
  return newSound
  

