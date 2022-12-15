file = open("9aclass.txt", encoding="utf8")
file1 = open("results.txt", 'a', encoding="utf8")
counter = 0
for line in file:
    line = str(line)
    grade = line[-2]
    if(grade == '4'):
        counter += 1

counter = str(counter)

file1.write("\n")
file1.write("\n")
file1.write("Учениците които имат оценка 4 са ")
file1.write(counter)
file1.write(" на брой.")
file.close()
file1.close()