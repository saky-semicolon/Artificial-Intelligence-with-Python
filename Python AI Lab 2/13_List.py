

# Lists can be created by enclosing comma-separated values in square brackets.

my_list = ["value1", "value2", "value3"]

# List items can be accessed by their index. The indexes start from 0. To access the first item in a list, you would use its index 0.

print(my_list[0])       #value1

# Lists can be modified by adding, removing, or changing elements.

# Elements can be added to the end of a list using the append() method.

my_list.append("value")
print(my_list)         #['value1', 'value2', 'value3', 'value']

# Elements can be removed from a list using the remove() method.

my_list.remove("value1")
print(my_list)         #['value2', 'value3', 'value']

# List:
thislist = ["apple", "banana", "cherry"]
print(thislist)        #['apple', 'banana', 'cherry']

# List that have repeatative item.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)        #['apple', 'banana', 'cherry', 'apple', 'cherry']

# List lenght.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))   #3


list1 = ["apple", "banana", "cherry"]   #String data type
list2 = [1, 5, 7, 9, 3]                 #Int data type
list3 = [True, False, False]            #Boolean data type
print(list1)                            
print(list2)
print(list3)

# A list can contain different types of data.
list1 = ["abc", 34, True, 40, "male"]

# From Python's perspective, lists are defined as objects with the data type 'list'. What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)         #['apple', 'banana', 'cherry']

#Access item-Printing the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])      #banana

#Negative Indexing- Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     #cherry

