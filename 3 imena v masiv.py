i = 0
ar = []

while i < 3: 
    a = input("Name: ")
    ar.append(a)
    i = i + 1

a = ar[2]
a = int(a)

if a > 5:
    print(ar)
