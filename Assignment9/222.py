# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
         return 0
        def h(root):
            if not root:
             return 0
            return h(root.left)+1
        l,r= h(root.left),h(root.right)
        if l==r:
            return (1<<l) +self.countNodes(root.right)
        else:
            return (1<<r)+self.countNodes(root.left)
