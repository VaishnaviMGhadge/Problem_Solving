arr=[1,2,3,4,5]
i=0
for j in range(1,len(arr)):
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
print(arr)