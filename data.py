a=[4,2,3]
b=[4,5,6]
sum1=0
sum2=0
i=0
j=0
while(i<3 and j<2):
    if(a[i]>b[j]):
        sum1+=1
        i+=1
        j+=1
    elif(a[i]<b[j]):
        sum2+=1
        i+=1
        j+=1
    elif(a[i]==b[j]):
        i+=1
        j+=1

print(sum1,sum2)
