# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        

    def helper(self, root, minimum, maximum):
        if root is None:
            return True
        if root.val >= maximum or root.val <= minimum:
            return False
        
        return self.helper(root.left, minimum, min(maximum, root.val)) and self.helper(root.right, max(minimum, root.val), maximum)
