# Manipulating Sounds
# Author: Vishesh Thakur
# February 19, 2016

#changeVolume () changes the volume of a sound by a given factor
#takes two input values: a sound to be modified and the factor 
def changeVolume(sound, factor):
  newSound = duplicateSound(sound)
  for s in getSamples(newSound):
    val = getSampleValue(s)
    setSampleValue(s, val * factor)
  return newSound

#fadeDown() this function slowly reduce the volume of a sound over time
#it takes two parameters: the sound to be modified, and the largest
#factor that the volume should be reduced by, which is a floating point number
def fadeDown (sound, factor) :
  newSound = duplicateSound(sound)
  curFactor = 1.0
  numberOfSamples = getNumSamples(newSound)
  for s in getSamples(newSound):
    val = getSampleValue(s)
    setSampleValue(s, val / curFactor)
    curFactor = curFactor + factor / numberOfSamples
  return newSound
  
#fadeUp() this function slowly increases the volume of a sound by 
#the desired amount. It takes two parameters: the sound to be modified
#and a floating point number that represents the max increase factor
def fadeUp (sound, factor) :
  newSound = duplicateSound(sound)
  curFactor = 1.0
  numberOfSamples = getNumSamples(newSound)
  for s in getSamples(newSound):
    val = getSampleValue(s)
    setSampleValue(s, val * curFactor)
    curFactor = curFactor + factor / numberOfSamples
  return newSound
 
  
#fadeIn() makes the initial portion of a sound quieter by some factor,
#and then gradually increases the volume until it reaches the original 
#level
def fadeIn(sound, factor) :
 newSound = duplicateSound(sound)
 curFactor = 1.0
 halfOfSamples = getLength(newSound) / 2
 for sampleIndex in range (0, getLength(newSound)):
   val = getSampleValueAt(newSound, sampleIndex)
   setSampleValueAt(newSound, sampleIndex, val / curFactor)
   curFactor = curFactor + factor / getLength(newSound)
 
 curFactor = 1.0
 for sampleIndex in range (halfOfSamples, getLength(newSound)):
   val = getSampleValueAt(newSound, sampleIndex)
   setSampleValueAt(newSound, sampleIndex, val * curFactor)
   curFactor = curFactor + factor / halfOfSamples
 
 return newSound
 
#version 2 of fadeIn() -- this is another way to solve the fadeIn problem
def fadeIn2(sound, factor) :
 newSound = fadeDown(sound, factor)
 curFactor = 1.0
 halfOfSamples = getLength(newSound) / 2
 for sampleIndex in range (halfOfSamples, getLength(newSound)):
   val = getSampleValueAt(newSound, sampleIndex)
   setSampleValueAt(newSound, sampleIndex, val * curFactor)
   curFactor = curFactor + factor / halfOfSamples
 
 return newSound

 
#cropSound(): crops a section of a sound and returns just the cropped 
#piece. This function takes as parameters the sound, the index to 
#start cropping, and the number of samples to include in the cropped sound
def cropSound(sound, start, numberSamples) :
  targetSound = makeEmptySound(numberSamples)
  end = start + numberSamples  #last sample to take from source sound
  targetIndex = 0
  for sourceIndex in range (start, end):
    value = getSampleValueAt(sound, sourceIndex)
    setSampleValueAt(targetSound, targetIndex, value)
    targetIndex = targetIndex + 1
  return targetSound
    
    
#cropSoundByTime: takes three parameters: the sound, the number of 
#seconds into the sound to start cropping, and the number of seconds 
#to include in the resulting sound
def cropSoundByTime (sound, secondsIn, totalSeconds) :
  samplingRate = int(getSamplingRate(sound))
  start = secondsIn * samplingRate #the starting sample in the source sound
  numberSamples = totalSeconds * samplingRate #the size of resulting sound
  targetSound = cropSound(sound, start, numberSamples)
  return targetSound
 


