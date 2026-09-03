# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,min,max):
        if root is None:
            return True
        if root.val<min or root.val>max:
            return False
        checkLeft = self.check(root.left,min,root.val-1)
        checkRight = self.check(root.right,root.val+1,max)
        return checkLeft and checkRight
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,-10000000000,10000000000)
        