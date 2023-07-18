# Python - Format - Strings
# String format: As we learned in the python Variables chapter, we cannot combine strings and numbers like this:
# Exampale: 

#ege = 30
#txt = "my name is Ghawsuddin, I am" + age
#print(age)

# But we can combine strings and numbers by using the [format()] method!
# The format() method takes the passed arguments, formats them, and places them in the string wehre the placeholders {} are:
# Example: Use the format() method to insert numbers inti strings:

age = 30
txt = "my name is Ghawsuddin, and i am {}"
print(txt.format(age))


# The formate() method takes unlimited number of arguments, and are placed into the respective placeholders:
# Example:
quantity = 3
itemno = 567
price = 49.95
myorder = " i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))


# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# Example: 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))