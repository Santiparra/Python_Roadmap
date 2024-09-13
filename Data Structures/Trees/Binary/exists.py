class BSTNode:
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)
        
################## Below CONTEXT code #################

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


################## Below Pseudo code #################
"""
Base Case: If the current node is None, the value doesn't exist in the tree, so return False.

Check the Current Node Value: If the value matches the current node’s value, return True.

Traverse the Left Subtree: If the value is less than the current node’s value, recursively check the left subtree.

Traverse the Right Subtree: If the value is greater than the current node’s value, recursively check the right subtree.

    
"""