class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        ans = 0

        while stack:
            node, cur = stack.pop()
            cur = cur * 10 + node.val
            if node.left is None and node.right is None:
                ans += cur
            if node.left is not None:
                stack.append((node.left, cur))
            if node.right is not None:
                stack.append((node.right, cur))

        return ans
