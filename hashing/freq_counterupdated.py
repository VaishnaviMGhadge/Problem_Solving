def freq_counter(num):
    hasharray=[0]*size
    for i in range(len(hasharray)-1):
        if(hasharray[l[i]]):
            hasharray[l[i]]+=1
        else:
            hasharray[l[i]]=1
    return hasharray[number]



if __name__=="__main__":
    size=int(input("enter size of an array"))
    l=[]
    for i in range((size)):
        ele=int(input('enter the element'))
        l.append(ele)

    query=int(input("how many query you want to check??"))
    while(query!=0):
        number=int(input('enter the number'))
        print(freq_counter(number))
        query-=1
