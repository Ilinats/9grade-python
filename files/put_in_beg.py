#Отново функция която приема име на файл и масив като аргументи. Функцията добавя
#съдържанието на масива като редове във файла, но ги добавя най-отпред.

def arr_lines(file_name, arr):
 
    for item in arr:
        with open(file_name, 'r+') as file: 
            item = str(item)
            file_data = file.read() 
            file.seek(0, 0) 
            file.write(item + '\n' + file_data) 
        file.close()
    
arr = [1, 2, 3]
arr_lines("put_pre_line.txt", arr)