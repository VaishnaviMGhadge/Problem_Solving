def isisorted(arr):
    f=False
    for i in range(len(arr)-1):
        if(arr[i]<=arr[i+1]):
            f=True
        else:
            f=False
            break
    if(f==True):
        print("array is sorted")
    else:
        print("array is not sorted")

isisorted([1,2,3,5,4])