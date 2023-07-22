print(100 > 50)
print(200 == 100)
print(350 < 250)

print(34 > 30)

a = 250
b = 150

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

Mustafa = 4
karim = 3

if karim > Mustafa:
    print("Karim is older than Mustafa")
else:
    print("Karim is not older than Mustafa")


Sadaf = 20
Rahim = 18


if Sadaf < Rahim:
    print("Sadaf is older than Rahim")
else:
    print("Sadaf is older than Rahim")


print(bool("Hello and Welcome"))
print(bool(25))

x = "Hello and welcome to my world!"
y = 25

print(bool(x))
print(bool(y))

a = "I amd 35 years old"
b = 35
print(bool(x))
print(bool(y))


bool("abcdef")
bool(123456)
bool(["Afghanistan", "Tajikistan", "USA", "Uzbekistan"])

print(bool("abcdef"))
print(bool(123456))
print(bool(["Afghanistan", "Tajikistan", "USA", "Uzbekistan"]))



print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))




def myclass():
   return True

print(myclass())



def myName() :
  return True

if myName():
  print("YES!")
else:
  print("NO!")


x = 400
print(isinstance(x, int))

y = 850
print(isinstance(x, int))

z = 4500
print(isinstance(z, int))




x = ["Ali", "Karim"]
y = ["Ali", "Karim"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

x = ["Muhamad", "Karim", "Rahim"]
y = ["Muhamad", "Karim", "Rahim"]
z = y
print(x is not z)
print(x  is not y)
print(y is not z)
print(x != y)



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y