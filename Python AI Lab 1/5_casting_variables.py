
#in the previous codes, we saw that it is not so necessary to assign the variables type in python to get the output.
#If we want to specify the data type of a variable, this can be done with casting.

x = str("4") # str() builds a string from a variety of data types, such as strings, integer literals, and float literals. 
y = int(4) # The int() function creates an integer from an integer literal a float literal (by truncating the decimal places), or a string literal (if the string is a whole number)
z = float(4) # z will be 4.0#float() builds a float from an integer literal, a float literal, or a string (if the string is a float or an integer).

print(x)
print(y)
print(z)

"""
If we want to specify the data type of a variable, this can be done woth casting-
"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = num1 + num2   # Input: 10, 20

print(sum)      # Output: 1020

"""
If we don't declare the variable type then it will show the variable data as a stribg by Default.
If it's not string then we should declare the data type.
"""

sum = int(num1) + int(num2)     # Input: 10, 20 
print("The result is", sum)     # Output: 30






