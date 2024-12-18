def counting(arr):
    maximum = max(arr)

    output = [0] * len(arr)
    count = [0] * (maximum + 1)

    for num in arr:
        count[num] += 1

    for i in range(1,len(count)):
        count[i] += count[i-1]

    for i in range(len(arr) - 1, -1,-1):
        output[count[arr[i]] -1 ] = arr[i]
        count[arr[i]] -= 1

    return output

print(counting([5,4,2,3,8,3]))    
