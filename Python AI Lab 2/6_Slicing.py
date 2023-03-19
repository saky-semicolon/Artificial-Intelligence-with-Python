
# Slicing in Python is a way to access elements of a sequence (list, tuple, string etc.) by specifying a range of indices. The syntax for slicing is: sequence[start:stop:step] 

# By default start is 0, stop is the length of the sequence, and step is 1. For example, a[3:7] will return elements from index 3 up to (but not including) index 7. 

b = "Hi! S M Asiful Islam Saky"
print(b[5:8])
print(b[8:15])
print(b[20:30])

# Slice From the Start
print(b[:10])

# Slice From the Start
print(b[15:])

# Negative Indexing
c = "Python is an easy programming language"
print(c[-15:-10])
