def BinarySearch(arr,ele):
    f=False
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]==ele):
            f=True
            break
        elif(arr[mid]<ele):
            low=mid+1
            f=False
        else:
            high=mid-1
            f=False
    if f==True:
        return f'element {arr[mid]} found at  location {mid+1}'
    else:
        return 'not found sorry:('
    

if __name__=="__main__":
    arr=[6,9,11,13,17]
    ele=60
    ans=BinarySearch(arr,ele)
    print(ans)  
    
