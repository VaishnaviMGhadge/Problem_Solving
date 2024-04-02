## print  all even till n 
n=int(input('enter the nnumber'))
c=1
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        c+=1
print(c)
    

## print all odd numbers upto n

for i in range(1,10):
    if(i%2!=0):
        print(i)


## print all the numbers divisible by 3 
for i in range(1,20):
    if(i%3==0):
        print(i)


## to store list of data use list
        
even=[]
for i in range(1,11):
    if(i%2==0):
        even.append(i)
print(even)
print(even[-1])
        
for i in range(len(even)):
    print(even[i])
