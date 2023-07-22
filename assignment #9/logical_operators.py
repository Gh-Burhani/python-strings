x = 55
y = 20
z = 60

print(x > y and x < z)



x = 10
y = 5

print(x > y or x < y)



x = 65
y = 68

print(x < y or x > y)


x = 15
y = 10
z = 20

print(not(x > y and x < z))


x = ["Ali", "Karim", "Samad"]
y = ["Ali", "Karim", "Samad"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["Ali", "Karim", "Samad"]
y = ["Ali", "Karim", "Samad"]
z = x

print(x is not z)
print(x is not y)
print(x != y)
