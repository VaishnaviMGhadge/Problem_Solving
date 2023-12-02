arr=[1,2,3,4,5]
for i in range(len(arr)):
    f=False
    if(arr[i]>=arr[i-1]):
        f=True
    else:
        f=False
        break
if(f==True):
     print(1)

else:
    print(0)