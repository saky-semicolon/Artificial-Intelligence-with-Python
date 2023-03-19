
# Concatenation is the process of joining two or more strings together to form one string.
# there are several methods for string concatenation. These include the use of the plus (+) operator, the join() method, and the format() method. 
# The plus (+) operator is the simplest way to concatenate two strings. For example:

firstName = "S M Asiful Islam"
lastName = "Saky"
# To add a space between them, add a " ":
fullName = firstName + " " + lastName
print(fullName)  # Output: S M Asiful Islam Saky

# The join() method is used to join two or more strings together. This method takes one argument, which is a list of strings. For example:

word1 = "Hello "
word2 = "World!"
word3 = "This is "
word4 = "Python."
sentences = " ".join([word1, word2, word3, word4])
print(sentences)  # Output: Hello World! This is Python

# The format() method is a powerful way to concatenate strings. It allows us to insert variables and other data types into a string. For example:

word1 = "Hello"
word2 = "World!"
sentence = "{} {}".format(word1, word2)
print(sentence)  # Output: Hello World