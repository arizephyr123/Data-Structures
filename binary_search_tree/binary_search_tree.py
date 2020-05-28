"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            #check if self.right already exists

            if self.right is not None:
                # if so, make that 
                # node call insert with the same value
                self.right.insert(value)

            # if not, create a node with that value, set as right child
            else:
                self.right = BSTNode(value)
        
        else:
            # check if left exists
            if self.left is not None:
            # if so, make that node call insert with same value
                self.left.insert(value)
            # if not create new node to left
            else:
                self.left = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # root could be target
        if target == self.value:
            return True
        
        elif target > self.value:
            if self.right is not None:
                # return recursion call to pass it back up to contains call at the root or bottom of the call stack
                return self.contains(target)
            else:
                return False

        else:
            return self.left.contains(target) if self.left is not None else False

        


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    # Call the function `fn` on the value of each node
    # how does child node know to return to the parent node? --> Incompleted parent node in call stack on top after child process completed and removed
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
