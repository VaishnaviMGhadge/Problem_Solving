def SelectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    return arr


if __name__=="__main__":
    arr=[9,11,3,2,5]
    ans=SelectionSort(arr)
    print(ans)