import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value

        current_node = self

        def insert_node(node, value):
                
            if value > node.value:
                if node.right is None:
                    node.right = BinarySearchTree(value)
                else:
                    insert_node(node.right, value)

            elif value < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(value)
                else:
                    insert_node(node.left, value)
        
        insert_node(current_node, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None: 
            return False

        current_node = self

        while current_node is not None:
            if current_node.value == target:
                return True
            elif current_node.value > target:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return
        else:
            current_node = self
            max_val = current_node.value
            while current_node is not None:
                if current_node.value > max_val:
                    max_val = current_node.value
                
                current_node = current_node.right
            
            return max_val

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

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

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
