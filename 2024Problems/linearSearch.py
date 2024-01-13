def linearsearch(arr,ele):
    f=False
    for i in range(len(arr)):
        if(arr[i]==ele):
            f=True
            break
        else:
            f=False

    if f==True:
        return f'element {arr[i]} found at  location {i+1}'
    else:
        return 'not found sorry:('
    

if __name__=="__main__":
    arr=[6,9,11,13,17]
    ele=11
    ans=linearsearch(arr,ele)
    print(ans)