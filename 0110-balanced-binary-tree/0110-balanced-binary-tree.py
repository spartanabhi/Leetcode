# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if abs(lheight - rheight)>1:
            self.ans = False

        return max(lheight,rheight)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
        