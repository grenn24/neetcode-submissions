# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def helper(curr: Optional[TreeNode], low, high):
            if curr is None:
                return True

            if not (low < curr.val < high):
                return False

            return helper(curr.left, low, min(curr.val, high)) and helper(curr.right, max(curr.val, low), high)
            

        return helper(root, float('-inf'), float('inf'))