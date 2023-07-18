# Python - Modify strings
# python has a set of built-in methods that you can use on strings

# Upper Case
# Example: the upper() method returns the string in upper case:

a = "Afghanistan"
print(a.upper())
 
b = "Hello, world!"
print(b.upper())

# Lower Case
a = "Afghanistan"
print(a.lower())

b = "Hello, World!"
print(b.lower())



# Remove Whitespace
# Whitespace is the space befor and/or after the actual text, and very often you want to remove this space.
# Example: the - strip() - method removes any whitespace frome the beginning or the end:
 
a = "Hello, World!"
print(a.strip()) # returns "Hello, World!"

#b = "Afghanistan is the   best  country in the world!"
print(b.strip())

# Replace String
# Example: the - replece()- method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

b = "Ghawsuddin"
print(b.replace("G", "F"))

# Split String
# The (split()) method returns a list where the text between the specified separator becomes the list items.
# Example: the split() method splits the string into substrings if it finds instances of the separator:

a = "hello, World!"
print(a.split(","))

b= "Afghanistan, is, great, Country"
print(b.split(","))