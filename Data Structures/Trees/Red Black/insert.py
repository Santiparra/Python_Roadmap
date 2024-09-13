class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
################## Above CONTEXT code #################

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

################## Below Pseudo code #################
"""
Create the new node

    Create a new RBNode from the given input value
    The new node shouldn't have a parent yet
    The new node's left and right children should be nil
    The new node is red. (new_node.red = True)

Find the parent of the new_node if there will be one

    Initialize a parent variable to None
    Initialize a current variable to the root node of the tree
    While current isn't a nil node:
        Set parent to the current
        If the new_node's value is less than the current node's, set current to its own left child. If it's greater, set to its right child. If the values are equal, just return because this value is a duplicate.
    parent should now be a reference to the node that will become the parent of the new node

Insert the new node

    Set the new node's parent to the parent we just found
    If the parent is None, we are dealing with a new root, so set the tree's root data member to the new node
    Otherwise, compare the values of the parent and new node and set the parent's left or right child based on the results

"""