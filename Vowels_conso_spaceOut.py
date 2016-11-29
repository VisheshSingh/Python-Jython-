# strings and for loops 
# CS 140 - Vishesh Thakur
# September 29, 2015

# Print a pyramid of an input character
def pyramid (character) :
  space = " "
  print 4 * space, character
  print 3 * space, 3 * character
  print 2 * space, 5 * character
  print space, 7 * character
  print 9 * character
  
#answer to the questions on which character lines up better  
# The character * lines up best as it is the closest in width 
# to the space character. All the other characters look lopsided 
# because they are much wider, meaning they extend far
# more to the right than they should to make the pyramid even.

# This function prints an inverted pyramid of an input character
def invertedPyramid (character) :
  space = " "
  print 9 * character
  print space, 7 * character
  print 2 * space, 5 * character
  print 3 * space, 3 * character
  print 4 * space, character
  
# justVowels2(): print only the vowels in piece of text
def justVowels2 (myString) :
  for letter in myString :
    if letter in "aeiouAEIOU" :
      print letter

# justVowels3(): print only the vowels in piece of text
def justVowels3 (myString) :
  for letter in myString :
    if letter.lower() in "aeiou" :
      print letter

# notVowels()
# this function should print only consonants but if
# the string contains vowels in uppercase, they get printed too
def notVowels (myString) :
  for letter in myString :
    if not (letter in "aeiou") :
      print letter
      
# notVowels2(): fixed so it only prints consonats
def notVowels2 (myString) :
  for letter in myString :
    if not (letter in "aeiouAEIOU") :
      print letter
      
# notVowels3(): fixed so it only prints consonats
# another possible solution using lower()
def notVowels3 (myString) :
  for letter in myString :
    if not(letter.lower() in "aeiou") :
      print letter

# splitLetters(): takes a string and separates the vowels from the
# consonants. It prints the vowels and the consonants in the 
# input string
# Note: This version explicitly checks for consonants, instead if a 
# character is not a vowel. A version in which that line is replaced 
# with: if not letter.lower() in "aeiou": would also be acceptable.
def splitLetters(myString):
  vowels= ""
  consonants = ""
  for letter in myString :
    if letter.lower() in "aeiou":
      vowels = vowels + letter
    if letter.lower() in "qwrtypsdfghjklzxcvbnm":
      consonants = consonants + letter
  print "Vowels: " + vowels
  print "Consonsants: " + consonants
  
#spaceItOut(): takes a string and an integer as its input
#it adds spaces in between each letter, then prints out the
#resulting string
def spaceItOut(aString, number):
  pile = ""
  space = " "
  for index in range(0, len(aString)-1) : #we don't want to add spaces after the last character 
    pile = pile + aString[index] + number * space
  pile = pile + aString[len(aString)-1]  #don't forget to concatenate the last character in the string
  print pile
