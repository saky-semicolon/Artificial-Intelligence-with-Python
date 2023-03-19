

# The range() function in Python is a built-in function that returns a sequence of integers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# The syntax for range() is: range(start, stop, step)
"""
start: this is the starting number of the sequence. If not specified, 0 is used as the start value.

stop: this is the end of the sequence, which is not included in the sequence.

step: this is the increment used to generate numbers in the sequence. If not specified, the default value is 1.
"""

for i in range(10):
    print(i)

# Output:
0
1
2
3
4
5
6
7
8
9

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        #['cherry', 'orange', 'kiwi']

# Change Item value:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)         #['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)         #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

