
# You can use the split() function to split a string in Python. 
# The syntax for the split() function is: string.split(separator, maxsplit).
# The separator is a character used to separate or split the string.
# The maxsplit parameter is used to limit the number of splits in the string. For example:

name = "S M Asiful Islam Saky"

#Split the string using the separator ' '
name_split = name.split(' ', 5)

#Print the split string
print(name_split)       #['S', 'M', 'Asiful', 'Islam', 'Saky']

#Example-2:

address = "AIU, Alor Setar, Kedah, Malaysia"

address_split = address.split(' ', 3)

print(address_split)        #['AIU,', 'Alor', 'Setar,', 'Kedah, Malaysia']

#Example-3:

languages = "HTML, CSS, JAVASCRIPT, C, PYTHON"

languages_split = languages.split(' ', 2)       #['HTML,', 'CSS,', 'JAVASCRIPT, C, PYTHON']

print(languages_split)
