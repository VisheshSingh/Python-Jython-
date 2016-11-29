from media import *
#useful functions to manipulate sounds
#Changing a sound volume by changing the amplitude
def changeVolume (sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue (sample)
    setSampleValue (sample, value * factor)
  
#Normalize a sound to a maximum amplitude
def normalize (sound):
  largest = 0 
  for s in getSamples(sound):
    largest = max (largest, getSampleValue(s))
  multiplier = 32767.0 / largest
  
  print "Largest sample value in original sound was " , largest
  print "Multiplier is " , multiplier
  
  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue (s, louder)
	
#clipping a sound:  we will clip a sound and copy the samples from end to start
def clip (source, start, end):
  target = makeEmptySound (end - start + 1) #create a new empty sound of this size
  targetIndex = 0 
  for sourceIndex in range (start, end + 1):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1
  return target
  
#Copying a sound:  we will copy a source sound into a target sound starting at index start
def copy (source, target, start):
  targetIndex = start 
  for sourceIndex in range (0, getLength(source)):
    sourceValue = getSampleValueAt (source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1
    
#reversing sounds: take a source sound and produce a sound with all the samples in reverse order
def reverse(source):
  target = makeEmptySound (getLength(source))
  sourceIndex = getLength (source) - 1  #we start at the end of the source sound, with the last sample
  for targetIndex in range (0, getLength(target)):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    sourceIndex = sourceIndex - 1
  return target
  
#mirroring sounds
def mirrorSound (sound):
  len = getLength(sound)
  mirrorPoint = len / 2
  for index in range (0, mirrorPoint):
    left = getSampleObjectAt(sound, index)
    right = getSampleObjectAt(sound, len - index - 1)
    value = getSampleValue(left)
    setSampleValue(right, value)
  play(sound)
