"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   A: 
"""
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if len(self.storage) == 0:
            return None

        popped_val = self.storage.remove_from_head()

        return popped_val
