class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self             
          
############################## CONTEXT code ##############################

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

############################## Pseudo code ##############################        
"""
    Check if the current node's value (self.val) is None.

      If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.

    If the value to delete (val) is less than the current node's value:

      Check if there's a left child (self.left). If it exists, recursively call the delete method on the left child with the value to delete and set the left child to the return value of the recursive call.
      Regardless of whether the left child exists or not, return the current node.

    Do the same (but mirrored) for the right child (self.right).
    If the value to delete is equal to the current node's value, we have found the node we want to delete:

      If there is no right child, return the left child. This effectively deletes the current node by bypassing it.
      If there is no left child, return the right child. This effectively deletes the current node by bypassing it.
      If there are both left and right children, find the minimum larger node (min_larger_node) by traversing down the left side of the right subtree. This is the node with the smallest value that is still larger than self.val.
        Replace self.val with min_larger_node.val.
        Delete min_larger_node.val from the right subtree and set the right child to the return value of the recursive call.

    Return the current node.
"""