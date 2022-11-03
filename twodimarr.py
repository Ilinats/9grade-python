arr = [[11, 12, 5, 2], [1, 6, 10], [10, 8, 12, 5], [12, 1, 8, 6]]
sum_arr = [1, 2, 3, 4]
sum = 0

for index, item in enumerate(arr):
    arr[index].sort()
    sum = 0
    
    for i in arr[index]:
        sum = sum + i
        
    sum_arr[index] = sum
    
print(sum_arr)
    
index_sum = len(sum_arr)
print(index_sum)

for i in range(index_sum):
    for j in range(0, index_sum - i - 1):
        if sum_arr[j] > sum_arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)