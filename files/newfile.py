#Създайте друг файл в същата папка и презапишете съдържанието на test.txt в него.

with open("test.txt", "r") as f:
    with open("copyoftest.txt", "w") as f1:
        for line in f:
            f1.write(line)
            
f.close()
f1.close()