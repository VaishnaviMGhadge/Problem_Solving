def BubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        issorted=True
        for j in range(i):
            if(arr[j]>arr[j+1]):
                issorted=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if(issorted==True):
            print("array is already sorted")
            break
    return arr

ans=BubbleSort([12,33,44,190])
print(ans)