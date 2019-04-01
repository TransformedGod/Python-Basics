#1

original_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for i in original_list:
    if i > 0 and (i ** 0.5).is_integer():
        new_list.append(int(i ** 0.5))
    else:
        pass
print(new_list)


#2

date = "02.11.2013"

days = { "01" : "первое", "02" : "второе", "03" : "третье"}
months = { "10" : "октября", "11" : "ноября", "12" : "декабря"}

for key, value in days.items():
    if key == date.split('.')[0]:
        day = value

for key, value in months.items():
    if key == date.split('.')[1]:
        month = value

print(f"{day.capitalize()} {month} {date.split('.')[2]} года.")


#3

import random

list=[]
n = int(input("Введите число: "))
for i in range(n):
    list.append(random.randint(-100, 100))
print(list)


#4

import random

list = []
for i in range(10):
     list.append(random.randint(0, 10))
print(list)

list_a = set(list)
print(list_a)

list_b = []
for i in list:
    if list.count(i) == 1:
        list_b.append(i)

print(list_b)