class Node:

    def __init__(self,data=None,nex=None):
        self.data=data
        self.next=next

    #set the data 
    def setData(self,data):
        self.data=data

    #get the data
    def getData(self):
        return self.data
    
    #set the next
    def setNext(self,next):
        self.next=next

    #get the next
    def getNext(self):
        return self.next
    

if __name__=='__main__':
    head=Node(23)
    node1=Node(25)
    node2=Node(89)
    tail=Node(89)

    head.setNext(node1)
    node1.setNext(node2)
    node2.setNext(tail)

    def Traverse(head):
        temp=head
        while(temp):
            print(temp.getData(),end='-->')
            temp=temp.getNext()
            
    Traverse(head)
    print("\n")