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
    node2=Node(5)
    node3=Node(6)
    node4=Node(7)


    head.setnext(node2)
    node2.setnext(node3)
    node3.setnext(node4)


    def traversing():
        temp=head
        while(temp!=None):
            print(temp.getdata(),end='-->')
            temp=temp.getnext()

    #traversing()


    def Recursion_Travelling(head):
        temp=head
        if(temp==None):
            return 
            
        else:
            print(temp.getdata())
            Recursion_Travelling(temp.getnext())
    #Recursion_Travelling(head)


    def Length_Of_LL(head):
        temp=head
        c=0
        while(temp!=None):
            c+=1
            temp=temp.getnext()
        print(c)
    
    #Length_Of_LL(head)


    def Length_Of_LL_Recursion(head):
        temp=head
        if(temp==None):
            return 0
        else:
            return 1+Length_Of_LL_Recursion(temp.getnext())
        
    #print(Length_Of_LL_Recursion(head))


    def InsertionAtBeginning(head):
        newnode=Node(8)
        newnode.setnext(head)
        head=newnode
        temp=head
        while(temp!=None):
            print(temp.getdata())
            temp=temp.getnext()
    
    #InsertionAtBeginning(head)


    def InsertionAtEnd(head):
        newnode=Node(23)
        temp=head
        if(temp==None):
            #print(temp.getdata())
            
            temp.setnext(newnode)
        else:
            temp=temp.getnext()
        temp1=head
        while(temp1!=None):
            print(temp1.getdata())
            temp1=temp1.getnext()
    InsertionAtEnd(head)


        

            



    
    

