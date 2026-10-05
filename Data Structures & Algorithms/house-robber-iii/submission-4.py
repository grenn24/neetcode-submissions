# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def helper(curr, isParent):
            if curr is None:
                return 0

            result = 0

            if (str(curr) + str(isParent)) in cache:
                return cache[str(curr) + str(isParent)]

            if isParent:
                result = helper(curr.left, False) + helper(curr.right, False)
            else:
                result = max(curr.val + helper(curr.left, True) + helper(curr.right, True), helper(curr.left, False) + helper(curr.right, False))

            cache[str(curr) + str(isParent)] = result
            return result

        return helper(root, False)