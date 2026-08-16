# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexDict = {}

        for index, num in enumerate(inorder):
            inorderIndexDict[num] = index

        def helper(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            rootVal = preorder[preLeft]
            inorderIndex = inorderIndexDict[rootVal]
            root = TreeNode(val=rootVal, left=None, right=None)

            root.left = helper(preLeft + 1, preLeft + (inorderIndex - inLeft), inLeft, inorderIndex - 1)
            root.right = helper(preLeft + (inorderIndex - inLeft) + 1, preRight, inorderIndex + 1, inRight)
            
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)