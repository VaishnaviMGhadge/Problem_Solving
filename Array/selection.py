def Selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr


if __name__=='__main__':
    ans=Selection_sort([12,3,4,56,6])
    print(ans)
