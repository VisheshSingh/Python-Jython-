# Manipulating Sounds 
# Author: Vishesh Thakur 
# November 1, 2016

#changeVolume () changes the volume of a sound by a given factor
#takes two input values: a sound to be modified and the factor 
def changeVolume(sound, factor):
  newSound = duplicateSound(sound)
  for s in getSamples(newSound):
    val = getSampleValue(s)
    setSampleValue(s, val * factor)
  return newSound
  
# What do you think the duplicateSound function does?  
# duplicateSound() creates and returns an exact copy of the sound passed to the function

#Do you think there is a similar function for images? 
# yes, theres is a duplicatePicture function that receives an image and returns an exact copy of it

#FadeDown() Design Questions: 
#What should the initial value of curFactor be? 1.0
#By how much should curFactor be increased after every sample? factor / numberOfSamples

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

 
#increaseDecrease(): increases the volume of all samples with positive values 
#and decreases the volume of all samples with negative values 
#Parameter: the sound to be modified 
def increaseDecrease (sound) :
  #find the largest sample in the original sound
  largest = 0
  for s in getSamples(sound) :
    largest = max(largest, getSampleValue(s))
  multiplier = 32767.0 / largest  #this is the factor to normalize each sample with a positive value
  
  newSound = duplicateSound(sound)
  for s in getSamples(newSound):
    value = getSampleValue(s)
    if (value >= 0) :  #a positive sample value
      setSampleValue(s, value * multiplier)
    else : #a negative sample value
      setSampleValue(s, 0)
      
  return newSound
  
# yes, the words in the speech can still be understood. The function produces a sound
#that is a little grainy / garbled.