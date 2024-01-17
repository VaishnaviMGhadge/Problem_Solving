import sys
def smallrec(arr,si):
   
    if(si>=len(arr)):
        return 99999
    else:
        min_ele=sys.maxsize
        if(arr[si]<min_ele):
            min_ele=arr[si]
            smallrec(arr,si+1)
        else:
            smallrec(arr,si+1)
ans=smallrec([3,5,2,1,4],0)
print(ans)