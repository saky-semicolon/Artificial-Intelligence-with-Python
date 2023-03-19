

#In programming, type conversion is the process of converting data of one type to another. There are two types of type conversion in Python--

#Implicit Conversion - automatic type conversion
#Explicit Conversion - manual type conversion


#For example: converting int data to str.


#Let's see some examples--

#Ex1- Converting integer to float
#Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#Output-

#Value: 124.23
#Data Type: <class 'float'>

#Ex2- Addition of string and integer Using Explicit Conversion

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


#Output-
#Data type of num_string before Type Casting: <class 'str'>
#Data type of num_string after Type Casting: <class 'int'>
#Sum: 35
#Data type of num_sum: <class 'int'>