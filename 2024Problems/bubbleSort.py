def BubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        issorted=True
        for j in range(i):
            if(arr[j]>arr[j+1]):
                issorted=False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if issorted==True:
            return 'already sorted'
        
    return arr

if __name__=="__main__":
    arr=[72,54,61,10,15,3]
    ans=BubbleSort(arr)
    print(ans)