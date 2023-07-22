#append

countrysList = ["Afghanistan", "Tajikistan", "USA", "Iran"]
countrysList.append("Pakistan")
print(countrysList)


fruitslist = ["apple", "banana", "cherry", "orange"]
fruitslist.append("Watermelon")
print(fruitslist)


#insert

countrysList = ["Afghanistan", "Tajikistan", "USA", "Iran"]
countrysList.insert(1, "Uzbekistan")
print(countrysList)


fruitslist2 = ["apple", "banana", "cherry", "orange", "melon", "mango"]
fruitslist2.insert(3, "Watermelon")
print(fruitslist2)


#Extend List

python_even = ["Shamsurahman", "Ghawsuddin", "Sadaf", "Atiq", "Ataullah"]
python_odd = ["Muhammad", "younus", "Jahanger","Ghafar"]

python_even.extend(python_odd)
print(python_even)



#Add Any Iterable
#we can add any iterable object (tuples, sets, dictionaries etc.)

countryslist4 = ["Afghanistan", "Tajikistan", "Iran"]
countrysList4tuple = ["Italy","Swedan"]

countryslist4.extend(countrysList4tuple)
print(countryslist4)


