# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(curr: TreeNode, visited: Set[int]):
            if curr is None:
                return
            newVisited = set(visited)
            newVisited.add(curr.val)
            filtered = list(filter(lambda x: x > curr.val, list(newVisited)))
       
            if len(filtered) == 0:
                self.result += 1
            
            
            helper(curr.left, newVisited)
            helper(curr.right, newVisited)

        self.result = 0
        helper(root, set())

        return self.result