n=int(input())
for i in range (n):
    for j in range (i,2*i+1):
        print((chr)(65+j),end=" ")
    print()

    