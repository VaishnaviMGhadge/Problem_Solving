def find_min(arr,si):
    if(si>=len(arr)):
        return 99999
    else:
        return min(arr[si],find_min(arr,si+1))

ans=find_min([2,3,1,4],0)
print(ans)