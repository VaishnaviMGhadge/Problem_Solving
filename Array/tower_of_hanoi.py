def Tower_of_Hanoi(n,s,d,a):
    if(n==1):
        return 1
    else:
        return Tower_of_Hanoi(n-1,s,a,d)+1+Tower_of_Hanoi(n-1,a,d,s)

if __name__=='__main__':
    print(Tower_of_Hanoi(4,'s','d','a'))