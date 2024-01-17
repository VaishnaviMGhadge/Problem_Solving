arr=[4,3,2,1,78,32,21,89]
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
