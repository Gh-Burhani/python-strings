# Python - Slicing Strings 
# Slicing: you ca return a range of characters by using the slince syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example: Get the charachters from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[2:5])

c = "Afghanistan"
print(c[3:11])

# Slice From  The Start
b = "Hello, World!"
print(b[:5])

c = "Afghanistan"
print(c[:6])

# Slice To the End
b = "Hello, World!"
print(b[2:])

c = "Afghanistan"
print(c[5:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example: Get the characters:
# From: "o"in"world!" (position-5)
# to, but not included: "d" in" world!"( position-2)

b = "Hello, World!"
print(b[-5:-2])

c = "afghanistan"
print(c[-11:-6])

d = "Ghawsuddin"
print(d[-10:-5]) 