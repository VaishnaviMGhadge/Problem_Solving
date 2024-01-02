def left_rotate(arr,k):
    temp=arr[:k]
    for i in range(k,len(arr)):
        arr[i-k]=arr[i]

    for i in range(len(arr)-k,len(arr)):
        arr[i]=temp[i-(len(arr)-k)]
    return arr

print(left_rotate([1,2,3,4,5],3))
