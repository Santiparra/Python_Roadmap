class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
################## Above CONTEXT code #################

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
    If the node doesn't have a value yet, just use the given value and be done
    If the node's value is equal to the given value, just be done, no duplicates allowed
    If the given value is less than the node's value and the node doesn't have a left child, create a new left child node with the given value
    If the given value is less than the node's value and the node does have a left child, recursively call insert on that left child
    Do the last two steps for the right child as well, but with the greater than comparison rather than less than
"""