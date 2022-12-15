#Напишете функция която приема 2 аргумента – името на нов файл, който ще бъде
#създаден и число „n“. Функцията трябва да създава нов файл със съответното име и да презаписва
#всеки n-ти ред от test.txt в него.

def lines(file_name, number_of_lines):
    counter = 1
    
    with open("test.txt", "r") as f:
        with open(file_name, "w") as f1:
            for line in f:
                if counter % number_of_lines == 0:
                    f1.write(line)
                    
                counter = counter + 1
        f1.close()
    f.close()
    
lines("nline.txt", 3)