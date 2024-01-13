def largest(arr):
    maxele=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>maxele):
            maxele=arr[i]
    return maxele


if __name__=="__main__":
    arr=[12,3,2,1,67]
    ans=largest(arr)
    print(ans)