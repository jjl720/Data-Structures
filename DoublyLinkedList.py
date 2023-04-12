class DoublyLinkedList:
    
    class Node:
        def __init__(self, elem = None, next = None, prev = None):
            self.data = elem
            self.prev = prev
            self.next = next
        
        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None
    
    def __init__(self):
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def add_after(self, node, elem): # theta(1)
        prev_node = node
        next_node = node.next
        
        new_node = self.Node(elem)
        new_node.next = next_node
        new_node.prev = prev_node
        prev_node.next = new_node
        next_node.prev = new_node
        
        self.size += 1
        return new_node
        
    def add_first(self, elem): # theta(1)
        
        return self.add_after(self.header, elem)
    
    def add_last(self, elem): # theta(1)
        return self.add_after(self.trailer.prev, elem)
        
    def add_before(self, node, elem): # theta(1)
        return self.add_after(node.prev, elem)
        
    def delete_node(self, node): # theta(1)
        if(self.is_empty()):
            raise Exception("LinkedList is Empty!!!")
        
        return_value = node.data
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        node.disconnect()
        
        self.size -= 1
        return return_value
    
    def delete_first(self): # theta(1)
        
        return self.delete_node(self.header.next)
    
    def delete_last(self): # theta(1)
        return self.delete_node(self.trailer.prev)
    
    
    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next
            
            
    def __repr__(self):
        #[100 <---> 200 <---> 500]
        return "["+ " <---> ".join([str(each) for each in self])+"]"


    def __getitem__(self,i):
        
        " The run time for this would be O(1/2 N) so technically O(N)"
        " I was not sure if you wanted negative indexing included. But I wrote the negative indexing."
        if i > self.size or i < (self.size*-1):
            raise IndexError('Index out of range')
        if i < 0:
            i = ( self.size + (i) )
        if self.size//2 > i: # first half of the list
            start = self.header
            for i in range(i+1):
                start = start.next
            return start.data
        else: # must be in the second half of the list
            end = self.trailer
            for i in range((self.size - i)):
                end = end.prev
            return end.data
                
            

def remove_all(doublylinkedlist1, data):
    cursor = doublylinkedlist1.header.next
    while cursor is not doublylinkedlist1.trailer:
        if cursor.data == data:
            next_node = cursor.next
            doublylinkedlist1.delete_node(cursor)
            cursor = next_node
            
        else:
            cursor = cursor.next
    
    #pass
    

# =============================================================================
# 
# 
dll = DoublyLinkedList()
dll.add_last(0)
dll.add_last(1)
dll.add_last(2)
dll.add_last(3)
dll.add_last(4)
dll.add_last(5)
dll.add_last(6)
# 
# 
print(dll)  

# =============================================================================
        
        
        
        
        
