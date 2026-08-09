# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        queue = deque([(root, 1)])
        result = []
        tmp = []
        currentHeight = 1

        while queue:
            curr, height = queue.popleft()
            if height == currentHeight:
                tmp.append(curr.val)
            else:
                currentHeight += 1
                result.append(tmp)
                tmp = [curr.val]
            
            if curr.left:
                queue.append((curr.left, height + 1))
            
            if curr.right:
                queue.append((curr.right, height + 1))

        result.append(tmp)

        return result