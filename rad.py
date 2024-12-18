def count(arr,exp):
    output =[0]* len(arr)
    count = [0] * 10

    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10] += 1 

    for i in range(1,10):
        count[i] = count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    return output

def radix(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = count(arr,exp)

        exp *= 10
    return arr
