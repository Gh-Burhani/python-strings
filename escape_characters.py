# Pytho - Escape Characters
# Escape characters: To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# Expample: You wil get an error if you use double quotes inside a string that is surrounded by double quotes:


#txt = "We are the so-called"vikings" from the north."  
#print(txt)


# to fix this problem, use the escape character \":
# Example: The escape character allows you to use double quotes when you normally would not be allowed:


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


txt = "Badakhshan Province is so \"beautiful\" in Afghanistan/"
print(txt)

# Escape Characters
# Other escaple characters used in python:
# Single Quote \'
txt = 'it\'s alright.'
print(txt)


# Backslash \\
txt = "This will insert one \\ (backslash)."
print(txt)


# New Line \n

txt = "Hello\nworld!"
print(txt)

txt = "Afghanistan\nis \nso \nbeautiful"
print(txt)


# carriage Return

txt = "nice\rKabul"
print(txt)


# Tab \t

txt = "Hello\tWorld!"
print(txt)

txt = "Afghanistan\tTajikistan"
print(txt)

# Backspace \b

txt = "Hello \bworld!"
print(txt)

# From Feed \f

txt = "Hello\fWorld!"
print(txt)


# Octal value \ooo
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)


# Hex value \xhh
# A backslash followed by an 'x' and a hex number represents a hex value:

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)