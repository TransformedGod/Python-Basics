#1

fruits = ["яблоко", "банан", "киви", "арбуз"]
for index, value in enumerate(fruits, 1):
    print("{}. {}".format(index, value.rjust(6)))


#2

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = set(a) & set(b)
a = set(a) - c
print (list(a))


#3

original_list = [1, 4, 7, 8, 2, 4, 9, 3]
new_list = []
for i in original_list:
    if i % 2 == 0:
      new_list.append(i / 4)
    else:
      new_list.append(i * 2)
print(new_list)