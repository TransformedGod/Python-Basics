# Задание-1:

list_1 = [1, 2, 4, 0]
list_2 = [i**2 for i in list_1]
print(list_1,"-->",list_2)

# Задание-2:

list_1 = ["яблоки", "бананы", "киви", "ананасы"]
list_2 = ["яблоки", "арбузы", "киви", "манго"]

list_3 = [i for i in list_1 if i in list_2]
print(list_3)

# Задание-3:

list_1 = [i for i in range(-10, 100)]
list_2 = [i for i in list_1 if i % 3 == 0\
          and i > 0\
          and i % 4 != 0]

print(list_2)
