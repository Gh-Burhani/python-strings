my_list = []
print(my_list)



my_list = []
list1 = [10, 20, 30, 40, 50]

list2 = my_list + list1

print(list2)




my_list = []
list1 = [10, 20, 30, 40, 50]

for x in list1:
    my_list.append(x)
print(list1)



my_list = []
list1 = [10, 20, 30, 40, 50]

my_list.extend(list1)

print(my_list)



my_list = [10, 20, 30, 40, 50]
my_list.insert(1, 15)

print(my_list)


my_list = [10, 20, 30, 40, 50]
my_list[1: 4:] = ["15, 35"]

print(my_list)



my_list = [10, 20, 30, 40, 50, 60]
my_list[1: :4] = 15, 35

print(my_list)

