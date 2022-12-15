# Напишете функция, която приема име на файл и масив като аргументи. Функцията
# създава файла ако го няма и записва съдържанието на масива на отделни редове във файла. Ако
# файла съществува добавя елементите на масива като редове в файла.

def arr_lines(file_name, arr):
    
    with open(file_name, "a") as f:
        for item in arr:
            f.write("%s\n" % item)
    f.close()
    
arr = [1, 2, 3, 4, 5]
arr_lines("arr_lines.txt", arr)