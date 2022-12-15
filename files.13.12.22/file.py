file = open("9aclass.txt", encoding="utf8")
counter = 0
f1 = open("results.txt", 'w', encoding="utf8")
f1.write('Учениците, които имат оценка 6 са:')
    
for line in file:
    line = str(line)
    grade = line[-2]
    if(grade == '6'):
        counter = 0
        f1.write("\n")
        for word in line.split():
            counter += 1
            if(counter > 1 and counter < 4):
                f1.write(word)
                f1.write(" ")
            if(counter == 4):
                f1.write(word)
                f1.write(";")

file.close()
f1.close()                   