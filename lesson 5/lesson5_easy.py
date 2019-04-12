# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# for i in range(1,10):
#     try:
#         os.mkdir("dir_" + str(i))
#     except FileExistsError:
#         pass

#для нормала:
def cr_dir(path):
    os.mkdir(path)

path = ["dir_" + str(i) for i in range(1,10)]

for i in path:
    try:
       cr_dir(i)
    except FileExistsError:
        pass



# remove = os.listdir()
# for i in remove:
#     if i.startswith("dir_"):
#         os.rmdir(i)

#для нормала:
def del_dir(path):
    os.rmdir(path)

for i in path:
    try:
       del_dir(i)
    except NameError:
        print("Папки не найдены!")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_dir():
    list_dir = os.listdir()
    for i in list_dir:
        if os.path.isdir(i):
            print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

file = os.path.basename(__file__)
new_file, ex = file.split('.')

if __name__ == "__main__":
    shutil.copy(file, new_file + "_new" + "." + ex)