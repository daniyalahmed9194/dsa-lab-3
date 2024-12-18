def count(arr):
    n = len(arr)

    maxi = max(arr)
    output = [0]* n
    count = [0]  *( maxi + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] -1] = arr[i]
        count[arr[i]] -= 1
    
    return output

print(count([5,4,2,3,8,3]))