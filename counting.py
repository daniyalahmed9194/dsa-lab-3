def counting_sort(arr):
 
    max_val = max(arr)
    
    
    count = [0] * (max_val + 1)
    
   
    for num in arr:
        count[num] += 1
    
   
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
  
    output = [0] * len(arr)
    
   
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    
   
    for i in range(len(arr)):
        arr[i] = output[i]


arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)
counting_sort(arr)
print("Sorted array:", arr)
