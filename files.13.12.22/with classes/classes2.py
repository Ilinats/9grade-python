class Student:
    def __init__(self, first_name, second_name, last_name, grade):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.grade = grade
        
class TestGradeFileParsing:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, encoding="utf8")
        
    def file_parsing(self):
        students_list = []
        for line in self.file:
            line = str(line)
            word = line.split()
            students_list.append(Student(word[1], word[2], word[3], word[4]))
            
        return students_list
    
    def close(self):
        self.file.close()
        
class TestResults:
    def __init__(self, file_name, students):
        self.file_name = file_name
        self.students = students
        self.file = open(self.file_name, 'w', encoding="utf8")
        
    def analyze_grade_a(self):
        self.file.write('Учениците, които имат оценка 6 са:\n')
        
        for index, item in enumerate(students):
            if self.students[index].grade == '6':
                self.file.write(self.students[index].first_name)
                self.file.write(" ")
                self.file.write(self.students[index].second_name)
                self.file.write(" ")
                self.file.write(self.students[index].last_name)
                self.file.write("\n")
                
    def analyze_grade_4_count(self):
        self.file.write('\nУчениците, които имат оценка 4 са: ')
        counter = 0
        
        for index, item in enumerate(students):
            if self.students[index].grade == '4':
                counter += 1
        
        self.file.write(str(counter)) 
        
    def analyze_average_grade(self):
        self.file.write('\nСредната оценка е: ')
        avr = 0
        
        for index, item in enumerate(students):
            avr += int(self.students[index].grade)
            
        avr = avr/len(self.students)      
        self.file.write(str(avr)) 
        
        if avr > 4.50:
            self.file.write("\nТестът беше лесен")
        else:
            self.file.write("\nТестът беше труден")
        
    def close(self):
        self.file.close()
               
temp = TestGradeFileParsing("9aclass.txt")
students = temp.file_parsing()
temp.close()

temp = TestResults("results2.txt", students)
temp.analyze_grade_a()
temp.analyze_grade_4_count()
temp.analyze_average_grade()
temp.close()