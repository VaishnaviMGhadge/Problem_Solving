def insert(arr,ele):
    for i in range(len(arr)):
        if(arr[i]>=ele):
            return i
        else:
            pass
    
if __name__=='__main__':
    arr=[1,2,4,7]
    res=insert(arr,9)
    print(res)

