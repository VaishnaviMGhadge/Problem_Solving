def LInearSearch(arr,si,ele):
    if(si>=len(arr)):
        return -1
    else:
        if(arr[si]==ele):
             return (si)
        else:
            return LInearSearch(arr,si+1,ele)

print(LInearSearch([1,2,3,4],0,1))
