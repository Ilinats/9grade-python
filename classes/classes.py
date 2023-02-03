class Student:
    def __init__(self, first_name, second_name, last_name, grade):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.grade = grade
        
students = []
        
file = open("9aclass.txt", encoding="utf8")
for line in file:
    line = str(line)
    word = line.split()
    students.append(Student(word[1], word[2], word[3], word[4]))
file.close()

f1 = open("results.txt", 'w', encoding="utf8")
f1.write('Учениците, които имат оценка 6 са:\n')
counter = 0
avr = 0

for index, item in enumerate(students):
    if students[index].grade == '6':
        f1.write(students[index].first_name)
        f1.write(" ")
        f1.write(students[index].second_name)
        f1.write(" ")
        f1.write(students[index].last_name)
        f1.write("\n")
    elif students[index].grade == '4':
        counter += 1
    avr += int(students[index].grade)

avr = avr/len(students)

f1.write("\nStudents with 4 are: " + str(counter))
f1.write("\nAvarage grade is: " + str(avr))

if avr > 4.50:
    f1.write("\nThe test was easy")
else:
    f1.write("\nThe test was hard")

f1.close()