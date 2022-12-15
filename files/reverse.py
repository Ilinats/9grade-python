#Напишете функция, която презаписва съдържанието на test.txt по редове в нов файл, но
#в обратен ред. Бонус: изтрийте първия файл.

import os

def reverse_lines():
    with open("reverse.txt", "w") as f2:
        
        with open("test_copy.txt", "r") as f1:
            data = f1.readlines()   
        os.remove("test_copy.txt")
        
        data_2 = data[::-1]
        
        f2.writelines(data_2)
    
    f2.close()
    
reverse_lines()