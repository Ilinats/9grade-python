def sum_digits(n):
    suma = 0
    n = int(n)
    while n > 0:
        suma += n % 10
        n = n//10
    
    return suma

def number_to_list(n):
    arr = []
    n = int(n)
    
    while n > 0:
        a = n % 10
        arr.append(a)
        n = n // 10
    
    return arr[::-1]

def to_number(digits):
    n = digits[0]
    
    for i in range(1, 3):
        n = 10 * n + digits[i]
        
    return n

def fib_num(n):
    if n < 2:
        return n
    else:
        return (fib_num(n-1) + fib_num(n-2))
    
def is_number_balanced(n, digit):
    arr = []
    arr1 = []
    arr2 = []
    sum1 = 0
    sum2 = 0
    balanced = 0
    
    if n < 10:
        return 1
    
    arr = number_to_list(n)
    middle = digit // 2
    
    arr1 = arr[0:middle]
    arr2 = arr[middle:]
    
    for i in arr1:
        print(i)
        sum1 += i
        
    for i in arr2:
        sum2 += i
        
    if sum1 == sum2:
        balanced = 1
        
    return balanced

def is_decreasing(arr):
    isTrue = 1
    
    for i in range(1, 5):
        if arr[i-1] < arr[i]:
            isTrue = 0
            
    return isTrue

num = input("Number: ")
print(sum_digits(num))

num1 = input("Number 2: ")
print(number_to_list(num1))

digits = [1, 2, 3]
print(to_number(digits))

num2 = input("Number: ")
num2 = int(num2)
print(fib_num(num2))

num3 = input("Number: ")
num3 = str(num3)
digit = len(num3)
num3 = int(num3)
print(is_number_balanced(num3, digit))

arr = [5, 4, 3, 2, 3]
print(is_decreasing(arr))