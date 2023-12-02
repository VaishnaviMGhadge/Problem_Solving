def insertion(arr):
    for i in range(1,len(arr)):
        v=arr[i]
        j=i
        while(j>=1 and arr[j-1]>v):
            arr[j]=arr[j-1]
            j-=1
        arr[j]=v
    return arr
ans=insertion([2,4,1,2,3])
print(ans)