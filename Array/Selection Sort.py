arr=[13,2,1,4,5]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j],arr[j+1]
print(arr)