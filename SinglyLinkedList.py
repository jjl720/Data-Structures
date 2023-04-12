# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 20:06:19 2021

@author: Joao Ji Won Lee
"""

class SinglyLinkedList:
    
    class Node:
        
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
            
        def disconnect(self):
            self.data = None
            self.next = None
            
    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return (len(self) == 0)
    
    def add_after(self, node, val):
        ''' Creates a new node containing val as its data and adds
        it after an existing node in the SinglyLinkedList'''
        new = SinglyLinkedList.Node(val)
        new.next = node.next # Point the new node to the node after
        node.next = new # break node before new node and point to new node
        self.size +=1
        return new
        
        
        
    def add_before(self, node, val):
        ''' Creates a new node containing val as its data and adds
        it before an existing node in the SinglyLinkedList'''
        curr = self.header 
        for i in range(self.size):
            if curr.next == node:
                return self.add_after(curr,val)
            else:
                curr = curr.next
                
    def add_first(self, val):
        ''' Creates a new node containing val as its data and adds
        it to the front of the SinglyLinkedList'''
        return self.add_after(self.header,val)
    def add_last(self, val):
        ''' Creates a new node containing val as its data and adds
        it to the back of the SinglyLinkedList'''
        curr = self.header 
        for i in range(self.size):
                curr= curr.next
        return self.add_after(curr,val)
    
    def delete_node(self, node):
        ''' Removes an existing node from the SinglyLinkedList and
        returns its value'''
        
        curr = self.header.next
        self.size -=1
        
        for i in range(self.size):
            if curr.next == node:
                curr.next = node.next
                val = node.data
                node.disconnect
                return val
            else:
                curr = curr.next
                

    def delete_first(self):
        ''' Removes an existing node from the front of the
        SinglyLinkedList and returns its value'''
       
        return self.delete_node(self.header.next)
    
    def delete_last(self):
        ''' Removes an existing node from the back of the
        SinglyLinkedList and returns its value'''
        curr = self.header
        for i in range(self.size-1):
            curr = curr.next
        
        curr.next = None
        
        return 
            
        
    def __iter__(self):
        cursor = self.header.next
        while(cursor is not None):
            yield cursor.data
            cursor = cursor.next
            
    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self])+ "]"
    
