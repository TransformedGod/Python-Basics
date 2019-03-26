# Easy

#Задача 1
first = 1
second = 2
third = 3
print(first, second, third)

fourth = input("Введите цифру 4: ")
print(fourth)


# Задача 2
fifth = int(input("Введите число: "))
print(fifth + 2)


# Задача 3
age = int(input("Сколько вам лет? "))
if age >= 18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет!")


# Normal
#
# Задача1
x = int(input("Введите число от 1 до 9: "))
while x < 0 or x > 10:
    x = int(input("Введите корректное число! "))

print(x**2)


# Задача 2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
a = a + b
b = a - b
a = a - b
print(a, b)


#Hard
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")
age = int(input("Ваш возраст: "))
weight = int(input("Ваш вес: "))
state = " "

if age < 30 and 50 <= weight <= 120:
    state = "хорошее состояние"
elif 30 < age <= 40 and weight < 50 or weight > 120:
    state = "следует заняться собой"
elif age > 40 and weight < 50 or weight > 120:
    state = "следует обратится к врачу!"
else:
    state = "жить будете, голубчик!"

print(name, surname, ", ", "возраст: ", age, ", ", "вес: ", weight, " - ", state)