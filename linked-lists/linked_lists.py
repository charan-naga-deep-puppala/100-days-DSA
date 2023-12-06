class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertionAtBegining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next=self.head
            self.next=new_node

    def insertionAtIndex(self,data,index):
        new_node = Node(data)
        position = 0
        current_node = self.head
        while(current_node!=None and position+1 != index):
            position += 1
            current_node= current_node.next
        if current_node != None:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index Not Present.")

    def insertionAtEnd(self,data,index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        
        while(current_node.next!=None):
            current_node.next = current_node
        
        current_node.next = new_node