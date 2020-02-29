# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def isTreeSame(t1, t2):
    if t1 is None or t2 is None:
        if t1 is None and t2 is None:
            return True
        else:
            return False
    if t1.val != t2.val:
        return False
    else:
        return isTreeSame(t1.left, t2.left) and isTreeSame(t1.right, t2.right)


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if t is None:
            return False
        current_node = False
        if s.val == t.val:
            current_node = isTreeSame(s, t)
        if current_node:
            return current_node
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
