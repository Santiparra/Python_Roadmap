class BSTNode:
    def preorder(self, visited):
        if self.val:
            visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

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
    Visit the value of the current node by appending its value to the visited array
    Recursively traverse the left subtree
    Recursively traverse the right subtree
    Return the array of visited nodes
"""