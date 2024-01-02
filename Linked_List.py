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
    

    

    

if __name__=='__main__':
    head=Node(23)
    node1=Node(25)
    node2=Node(89)
    tail=Node(89)

    head.setnext(node1)
    node1.setnext(node2)
    node2.setnext(tail)

    def Traverse(head):
        temp=head
        while(temp):
            print(temp.getdata(),end='-->')
            temp=temp.getnext()
            
    Traverse(head)
    print("\n")



    """def Recursion_Travelling(head):
        if not head:
            return
        else:
            print(head.getdata(),end='-->')
            return Recursion_Travelling(head.getnext())
        
    Recursion_Travelling(head)

    print("\n")


    def Length_Of_LL(head):
        temp=head
        c=0
        while(temp):
            c+=1
            temp=temp.getnext()
        print(c)
    
    Length_Of_LL(head)
    print("below is the recursiove approach")


    def Length_Of_LL_Recursion(head):
        if not head:
            return 0
        else:
            return 1+Length_Of_LL_Recursion(head.getnext())
        
        
    ans=Length_Of_LL_Recursion(head)
    print(ans)

def insertNode(head,data,k):
    #If the k is valid
    if (k > Length_Of_LL(head) or k <0):
        print("Argument k passed is not valid")
        return head

    #Create new node for data
    newNode = Node(data) #Create the new node object

    if( k==0):
        #We need to insert at the begining
        #We need to update the head
        newNode.setNext(head)
        head = newNode
    else :
        #When not in begining
        # We need to jump to the prev node of the postion
        prev = head
        i=0
        while(i<k-1):
            prev = prev.getNext()
            i+=1

        #prev will be one position left of kth position
        newNode.setNext(prev.getNext())
        prev.setNext(newNode)
    return head"""








