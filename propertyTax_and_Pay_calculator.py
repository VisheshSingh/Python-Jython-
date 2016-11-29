# Functional Decomposition and while Loops
# Author: Vishesh Thakur 
# November 12, 2015

#input validation loops

#This function calculates the retail prices -- without input validation
def retailPrices() :
  MARK_UP = 1.5 #this is a constant for the markup percentage
  
  #variable that controls the loop
  anotherItem = "Y"
  
  #loop to process one or more items
  while anotherItem == "Y" or anotherItem == "y" :
    #get the item's wholesale cost
    wholesaleCost = requestNumber("Please enter the item's wholesale cost")
    #calculate the retail price
    retail = wholesaleCost * MARK_UP
    #display retail price
    printNow("Retail Price:")
    printNow(retail)
    #Do this again?
    anotherItem = requestString("Do you have another item? (Y/N)")
  
  #end of the function
  printNow("Thanks for using the retail price calculator")
    
 
#Solution to problem 1
#This function calculates the retail prices -- with input validation
def retailPrices() :
  MARK_UP = 1.5 #this is a constant for the markup percentage
  
  #variable that controls the loop
  anotherItem = "Y"
  
  #loop to process one or more items
  while anotherItem == "Y" or anotherItem == "y" :
    #get the item's wholesale cost
    wholesaleCost = requestNumber("Please enter the item's wholesale cost")
    
    #validate input
    while wholesaleCost < 0 :
      #printNow("Error: The cost cannot be negative.")
      showError("Error: The cost cannot be negative.")
      wholesaleCost = requestNumber("Please enter the correct wholesale cost")
    
    #calculate the retail price
    retail = wholesaleCost * MARK_UP
    #display retail price
    printNow("Retail Price:")
    printNow(retail)
    #Do this again?
    anotherItem = requestString("Do you have another item? (Y/N)")
  
  #end of the function
  printNow("Thanks for using the retail price calculator")


#
#propertyTax(): requests information from the user, calls the calculateTax() function 
#and then shows the results.  Loops until the user decides to quit.
def propertyTax() :
  printNow("*** Welcome to the Property Tax Calculator ***")
  #variable that controls the loop
  again = "YES"
  #ask the user to enter the tax percentage
  taxPercentage = requestNumber("Please enter the tax percentage (e.g.: 2.0)")
  
  #loop to perform the calculations as many times as the user needs/wants
  while (again == "YES") :
    #ask the user to enter the property number
    propertyNumber = requestInteger("Please enter the property number")
    #validate property number
    while propertyNumber < 0 :
      showError("Error: The property ID cannot be negative.")
      propertyNumber = requestNumber("Please enter the property ID")
    
    #ask the user to enter the property value
    propertyValue = requestNumber("Please enter the property value")
    #validate property value
    while propertyValue < 0 :
      showError("Error: The property value cannot be negative.")
      propertyValue = requestNumber("Please enter the correct property value")
    
    #call the propertyTax function
    propertyTax = calculateTax(propertyValue, taxPercentage)
    
    #Show the results
    printNow ("The property tax for property number ")
    printNow (propertyNumber)
    printNow ("Valued at ")
    printNow (propertyValue)
    printNow(" is " )
    printNow (propertyTax)
    
    #ask the user if he/she wants to go again
    again = requestString("Do you need to perform another calculation? (YES/NO)")
    printNow("*******************************")
  
  #good bye message and end the program
  printNow ("Thanks for using the Property Tax Calculator Program. Good-Bye!")

#calculateTax(value, percentage): receives two floating point numbers and
#returns the calculated tax on a property using the formula:
#propertyTax = propertyValue * taxPercentage / 100.0
def calculateTax(value, percentage):
  tax = value * percentage / 100.0
  return tax


#Modularizing with functions
#main(): this is the top level function. It organizes and calls the other functions
def main() :
  #Get the amount of sales
  sales = getSales()
  
  #Get the amount of advanced pay
  advancedPay = getAdvancedPay()
  
  #Determine the commission rate
  commissionRate = determineCommissionRate(sales)
  
  #Calculate the pay
  pay = sales * commissionRate - advancedPay
  
  #Display the amount of pay
  print 'Monthly Sales: $', sales
  print 'Advanced Pay: $', advancedPay
  print 'The pay is: $', pay
  
  #Determine whether the pay is negative
  if pay < 0 :
    print("The salesperson must reimburse the company")
    
#getSales(): gets a salesperson's monthly sales form the user  
#and returns that value
def getSales() :
  #read the amount monthly sales
  monthlySales = requestNumber("Please enter the monthly sales for this employee")
  
  #validate input
  while monthlySales < 0 :
    showError("Error: The monthly sales cannot be negative.")
    monthlySales = requestNumber("Please enter the correct monthly sales for this employee")
  
  #Return the amount entered
  return monthlySales
  
#getAdvancedPay(): gets the amount of advanced pay given to the salesperson
#and returns that amount
def getAdvancedPay() :
  #read the amount of advanced pay
  advanced = requestNumber("Please enter the amount of advanced pay, or 0 if no advanced pay was given")
  
  #validate input
  while advanced < 0 or advanced > 2000.00:
    showError("Error: The advanced pay cannot be a negative number or more than $2000.00.")
    advanced = requestNumber("Please enter the advanced pay for this employee")
    
  #Return the amount entered
  return advanced
  
#determineCommissionRate(): accepts the amount of sales and returns the applicable
#commission rate
def determineCommissionRate(sales):
  #determine commission rate based on table
  if sales < 10000.00 :
    rate = 0.10
  elif sales >= 10000.00 and sales <= 14999.99 :
    rate = 0.12
  elif sales >= 15000.00 and sales <= 17999.99 :
    rate = 0.14
  elif sales >= 18000.00 and sales <= 21999.00 :
    rate = 0.16
  else :
    rate = 0.18
  
  #return the commission rate
  return rate

  
