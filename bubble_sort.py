def bubble_sort(arr):
    
    for i in range(len(arr)-1,0,-1):
        issorted=True
        for j in range(i):
            if(arr[j]>arr[j+1]):
                issorted=False
                arr[j],arr[j+1]=arr[j+1],arr[j]

        if issorted:
             return('array is already sorted',arr)
             
        
        else:
            return arr



if __name__=='__main__':
    ans=bubble_sort([2,3,4,21])
    print(ans)