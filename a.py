a = [[3, 4, 5], [7, 14, 2]]
b = 0
   
for i, el in enumerate(a):
    b += max(a[i])
    
print(b)