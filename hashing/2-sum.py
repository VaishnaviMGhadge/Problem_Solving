def twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if((arr[i]+arr[j])==target):
                return i,j
            
if __name__=="__main__":
    arr=[2,7,11,15]
    target=26
    print(twosum(arr,target))