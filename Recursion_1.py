def PrintRecur(arr,SI):
    if(SI>=len(arr)):
        print("done")
        return -1
    else:
        print(arr[SI])
        PrintRecur(arr,SI+1)

PrintRecur([1,2,3,4],0)