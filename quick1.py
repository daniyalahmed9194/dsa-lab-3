def quick(arr,start,end):
    if start < end:
        pivot = Partition(arr,start,end)
        quick(arr,start,pivot- 1)
        quick(arr,pivot+1,end)
def Partition(arr,start,end):
    p = arr[start]
    i = start + 1
    j = end
    while True:
        while i < end and arr[i] <= p:
            i += 1
        while j >= start and arr[i] > p:
            j += 1
        if i >= j :
            break
        arr[i],arr[j] = arr[j],arr[i]
        arr[start], arr[j], arr[j], arr[start]
    return j