#strings in python are surrounded by either single quotation marks, or double quotation marks.
#like: 'hello' or "hello"

print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Afghanistan is the must beutiful country in the world, it has alot of mountian and rivers"""
print(a)


a = '''Afghanistan is the must beutiful country in the world, it has alot of mountian and rivers'''
print(a)



#strings are Arrays
#like many other popular programming languages, strings in python are arrays of bytes representing unicode characters.
#However, python does not have a character data type, a singlte character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
#Example: Get the character at position 1 (remmeber tha the first character has the position 0):

a = "Hello, World!"
print(a[1])

b = "Ghawsuddin"
print(b[9])

#Looping Through a String 
#since stings are arrays, we can loop through the characters in a string, with a for loop
#Example: loop through the letters in the word "banana":

for x in "banana":
    print(x)

for y in "Afghanistan":
    print(y)


#String Length
#To get the length of a string, use the Len() function.
#Example: the len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

b = "Ghawsuddin Burhani."
print(len(b))

c = "Afghanistan"
print(len(c))

#Chech String 
#To check if a certain phrase or character is present in a string, we can use the keyword (in).
#Example: check if "free" is present ifn the following text:

txt = "the best things in life are free!"
print("free" in txt)

#Use it in an (if) statement:
#Example: pring only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
    print("yes, 'free' is present. ")

    #Check if Not
    # To check if a certain phrase or character is NOT present in a string, we can use the keyword NOT In.
    # Expample: Check if "expensive" is NOT present in the following text:

    txt = "the best things in life are free!"
    print("expensive" not in txt)

    # Use it in an (if) statement:
    # Example: prin only if "expensive" is NOT present

    txt = "the best things in life are free!"
    if "expensive" not in txt:
        print("no, 'expensive' is not present.")

    txt = "Afghanistan is the best Country in the world"
    print("great" not in txt)

    txt = "Afghanistan is the best Country in the world"
    if "great" not in txt:
        print("no, 'great' is not present")

