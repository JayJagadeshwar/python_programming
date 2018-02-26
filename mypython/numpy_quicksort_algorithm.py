def quicksort(arr):
    if len(arr) <1:
        return arr
    a = arr[len(arr)//2]
    l = [x for x in arr if x < a]
    m = [x for x in arr if x == a]
    r = [x for x in arr if x > a]
    return quicksort(l)+m+quicksort(r)

print(quicksort([9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,1]))
