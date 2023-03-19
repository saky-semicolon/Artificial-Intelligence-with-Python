
# Escape Sequence:
# The most common escape characters in Python are:
# • \n: Newline
# • \t: Tab
# • \': Single Quote
# • \": Double Quote
# • \\: Backslash
# • \a: Audible Alert
# • \b: Backspace
# • \f: Form Feed
# • \r: Carriage Return
# • \v: Vertical Tab
# • \ooo: Octal Value
# • \xhh: Hex Value


# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "We are the so-called \'Vikings\' from the north."
print(txt)
txt = "We are the so-called \n Vikings from the north."
print(txt)
txt = "We are the so-called \t Vikings from the north."
print(txt)
txt = "We are the so-called \b Vikings from the north."
print(txt)





