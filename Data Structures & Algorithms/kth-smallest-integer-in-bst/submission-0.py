# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    level = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        result = self.kthSmallest(root.left, k)
        if result != -1:
            return result
        
        self.level += 1
        if self.level == k:
            return root.val
        return self.kthSmallest(root.right, k)