def reverse(arr,si,ei):
    if(si>ei):
        return 
    else:
        
        arr[si],arr[ei]=arr[ei],arr[si]
        reverse(arr,si+1,ei-1)
ans=(reverse([1,2,3,4],0,3))
print(ans)