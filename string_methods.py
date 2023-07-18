# Python - String Methods
# String Methods: Python has a set of built-in methods that you can use on strings.
# NOte: All string methods return new values. They do not change the original string.

# Capitalize()
# Description: converts the first character to upper case
# Example: Upper case the first letter in this sentence:

txt = "hello, and welcom to my world."
x = txt.capitalize()

print(x)

txt = "afghanistan is the must beautiful contry in the world."
x = txt.capitalize()

print(x)

txt = "pytho is FUN!"
x = txt.capitalize()
print(x)

txt = "afghanistan is BEAUTIFUL Country"
x = txt.capitalize()
print(x)

txt = "my Daughter is the must bEAUTIFUL"
X = txt.capitalize()

print(X)


txt = "36 is my age."
x = txt.capitalize()

print(x)



# Casefold() method;  Converts string into lower case

txt = "Hello, And Welcome To My World!"
x = txt.casefold()

print(x)

txt = "Afghanistan Is The Must Beautiful Country In The World"
x = txt.casefold()

print(x)


# Center() method; Returns the number of times a specified value occurs in a string
# Example: print the world "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"
x = txt.center(50)

print(x)


txt = "banana"
x = txt.center(20, "0")
print(x)


# Count() Method: Returns the number of times a specified value occurs in a string

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")

print(x)

txt = "Afghanistan is the must beautiful country, in Afghanistan we have a home, also Afghanistan has alot of provinces"
x = txt.count("Afghanistan")

print(x)


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)

print(x)

