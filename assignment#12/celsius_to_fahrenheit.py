def celsius_to_fahrenheit(celsius = 25):
    fahrenheit = celsius * (9/5) + 32
    print(fahrenheit)

celsius_to_fahrenheit(32)
celsius_to_fahrenheit(0)



def cel_to_fah(celsius):
    return(celsius*1.8)+32
celsius = 25
print("fahrenheit is: ",int(cel_to_fah(celsius)))



celsius =25

fahrenheit = (celsius * 1.8) + 32

print("%.2f culsius = %.2f Fahrenheit" %( celsius, fahrenheit ))