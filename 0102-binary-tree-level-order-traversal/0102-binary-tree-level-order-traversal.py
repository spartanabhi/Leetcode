# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x = self.q[self.front]
        self.front +=1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
    def size(self):
        if self.front ==-1:
            return 0
        return len(self.q)-self.front
queue = Queue()
    


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        qu = Queue()
        qu.push(root)
        ans.append([root.val])
        while qu.size()>0:
            l = qu.size()
            level = []
            for i in range(l):
                front = qu.pop()
                if front.left != None:
                    qu.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    qu.push(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                ans.append(level)
        return ans

        