from datetime import datetime
now = datetime.now()
now = str(now)

file = open("9aclass.txt", encoding="utf8")
file1 = open("results.txt", 'a', encoding="utf8")
counter = 0
avr = 0

file1.write("\n")
file1.write("\n")
file1.write("Средно аритметичната оценка е: ")

for line in file:
    line = str(line)
    if counter != 24:
        grade = line[-2]
    else:
        grade = line[-1]
    temp = ord(grade) - 48
    avr += temp
    counter += 1

avr = avr / counter
file1.write(str(avr))
file1.write("\n")

if avr < 4.5:
    file1.write("Контролното беше трудно!")
else: 
    file1.write("Контролното беше лесно!\n")

file1.write("\n")  
file1.write("Date and time now:\n")  
file1.write(now)
    
file.close()
file1.close()