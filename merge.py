def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    L = mergesort(arr[:mid])
    R = mergesort(arr[mid:])
    return merge(L,R)

def merge(L,R):
    i = j =0
    result = []
    while(i < len(L) or j < len(R)):
        if L[i] < R[i]:
            result.append(L[i])
            i += 1

        else:
            result.append(R[j])
            j += 1

    while j < len(R):
        result.append(R[j])
        
    while i < len(L):
        result. append(L[i])
        i+=     1

    return result