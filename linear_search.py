def linear_Search(arr,ele):
    f=False
    for i in range(len(arr)):
        if(arr[i]==ele):
            f=True
            break
        else:
            f=False

    if(f==True):
        return 'element found at ',i+1,'position'
    else:
        return 'not found'
    
ans=linear_Search([12,34,56,78],120)
print(ans)
    

