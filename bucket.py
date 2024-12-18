def bucketsort(arr, k):
    buckets = [[] for _ in range(k)]
    for num in arr:
        index = k * num
        if index >= k:
            buckets[k - 1].append(num)
        else:
            buckets[index].append(num)
    
    for i in range(k):
        buckets[i] = insertionsort(buckets[i])

    result = []
    for bucket in buckets:
        for num in bucket:
            result.append(num)
    return result
