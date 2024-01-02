def rotate_k_times(arr,k):
    k=k%len(arr)


    ## reverse the entire array
    arr=arr[::-1]

    ## reverse the first k elements
    arr=arr[:k:-1]

    ## reverse the last k elements
    arr=arr[k::]
     
    return arr

print(rotate_k_times([1,2,3,4],2))