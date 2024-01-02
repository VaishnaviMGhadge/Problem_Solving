class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def setdata(self,data):
        self.data=data

    def getdata(self):
        return self.data
    
    def setnext(self,next):
        self.next=next

    def getnext(self):
        return self.next
    


if __name__=="__main__":
    head=Node(3)
    node1=Node(4)
    node2=Node(5)
    node3=Node(6)
    newnode=Node(1)
    newnode1=Node(7)

    head.setnext(node1)
    node1.setnext(node2)
    node2.setnext(node3)

    def traversing(head):
        temp=head
        while(temp!=None):
            print(temp.getdata(),end='-->')
            temp=temp.getnext()
    print('normal ordering is ')
    traversing(head)
    print("\n")

   

    def traverseRecursive(head):
        temp=head
        if(temp==None):
            return
        else:
            print(temp.getdata(),end='-->')
            traverseRecursive(temp.getnext())
    print("recursive ordering is :")       
    traverseRecursive(head)

    print("\n")

    def lengthofLL(head):
        temp=head
        c=0
        while(temp!=None):
            c+=1
            temp=temp.getnext()
        print("the number of nodes in the linked list is ",c)
    
    lengthofLL(head)


    print("\n")

    def lengthofLLRecursive(head):
        temp=head
        if(temp==None):
            return 0
        else:
            return 1+lengthofLLRecursive(temp.getnext())

    print("length of the linked list using recursion is ",lengthofLLRecursive(head))


    def InsertionAtBeginning(head):
        
        newnode.setnext(head)
        head=newnode
        traversing(head)
        #return head
    InsertionAtBeginning(head)


    def InsertionAtEnd(head):
        temp=head
        while(temp!=None):
            print(temp.getdata())
            temp=temp.getnext()
        temp.setnext(newnode1)
        traversing()
    
    print(InsertionAtEnd(head))
        
    


    




    

