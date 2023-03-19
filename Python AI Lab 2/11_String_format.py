
# The format() method of strings allows you to format selected parts of a string. 

# This method is used to format strings in Python. For example, 
#if you have a string like "Hello, my name is {name} and I am {age} years old.", you can pass the values of the variables name and age to the format() method to get the final string like "Hello, my name is John and I am 20 years old."

# Syntax: string.format(value1, value2, ...)


name = "Saky"
age = 19
prog = "Computer Science"
varsity = "AIU"
address = "Alor Setar, Kedah, Malaysia"

print("Hello, my name is {} and I am {} years old. I am studying {} in {}. I live in {}".format(name, age, prog, varsity, address)) 

# Output: Hello, my name is Saky and I am 19 years old. I am studying Computer Science in AIU. I live in Alor Setar, Kedah, Malaysia

