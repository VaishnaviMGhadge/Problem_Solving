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

    
    

