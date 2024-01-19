def upperBound(arr: [int], x: int) -> int:
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]>x):
            ans=mid
            high=mid-1

        else:
            low=mid+1

    return ans
    
if __name__=="__main__":
    arr=[1,3,3,4,7,9,11,13,15]
    
    res=upperBound(arr,11)
    print(res)