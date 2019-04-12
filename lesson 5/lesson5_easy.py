# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1,10):
    try:
        os.mkdir("dir_" + str(i))
    except FileExistsError:
        pass

remove = os.listdir()
for i in remove:
    if i.startswith("dir_"):
        os.rmdir(i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

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