#=================================== Program Lab1C.py =================================
# Program Lab1C.py
# Demonstrate the use of the input function to read numeric data.
# Calculates fuel efficiency based on values entered by the user.
miles = input ("Enter the number of miles: ")
gallons = input ("Enter the gallons of fuel used: ")
mpg = int (miles) / float (gallons)
print ("Miles Per Gallon: " + str (mpg))