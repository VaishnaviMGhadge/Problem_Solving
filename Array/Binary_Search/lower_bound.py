def lower_bound(arr,ele):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]>=ele):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


if __name__=="__main__":
    res=lower_bound([1,2,3,3,5,8,8,10,10,10,11],10)
    print(res)