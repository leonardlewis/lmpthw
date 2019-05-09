# Binary search trees allow fast insertion and binary search.
# Sorted arrays allow binary search but not fast insertion.
# Sorted lists allow fast insertion but not binary search.
# Every data structure is associated with an invariant.

class BSTreeNode(object):
    def __init__(self, parent, left, right, key, value):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key
        self.value = value

class BSTree(object):
    def __init__(self):
        self.root = None

    def get(self, key):
        """Given a key, walk the tree to find the node, or return None if you
        reach a dead-end."""

        node = self.root

        while node:
            if key < node.key:
                # Check that left node exists.
                if self.left == None:
                    return None
                else:
                    self.left.get()
            else:
                if key == self.key:
                    return (self.key, self.value)
                else:
                    # Check that right node exists.
                    if self.right == None:
                        return None
                    else:
                        self.right.get()

    def set(self, key, value):
        """Given a k-v, walk the tree to find the node, append a new node."""
        if self.get(key) == None:
            # Append the value if it's not there.


        else:
            return (key, value)
