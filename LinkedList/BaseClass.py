class Node:

    def __init__(self,data=None,nex=None):
        self.data=data
        self.next=next

    #set the data 
    def setdata(self,data):
        self.data=data

    #get the data
    def getdata(self):
        return self.data
    
    #set the next
    def setnext(self,next):
        self.next=next

    #get the next
    def getnext(self):
        return self.next
    

   
    

"""class Traverse(Node):
    def __init__(self,data=None,next=None):
        self.node=Node()
        super().__init__(data,next)

    def setdata(self,data):
        super().setdata(data)

    def getdata(self):
        super().getdata()

    def setnext(self, next):
        super().setnext(next)

    def getnext(self):
        super().getnext()"""

    
    

    
    


    

if __name__=="__main__":
    #creating the nodes 
    head=Node()
    head.setdata(3)
    node2=Node()
    node2.setdata(4)
    node3=Node()
    node3.setdata(5)

    #creating the linkages
    head.setnext(node2)
    node2.setnext(node3)


    def Traverse(head):
        temp=head
        while(temp):
            print(temp.getdata(),end='-->')
            temp=temp.getnext()
            
    Traverse(head)
    print("\n")






    

        