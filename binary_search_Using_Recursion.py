def binary_search(arr,left,right,ele):
    if(left>=right):
        return -1
    else:
        mid=int(left+(right-left)/2)
        if(arr[mid]==ele):
            return mid
        elif(arr[mid]>ele):
            return binary_search(arr,left,mid-1,ele)
        else:
            return binary_search(arr,mid+1,right,ele)

print(binary_search([1,2,3,45],0,4,19))