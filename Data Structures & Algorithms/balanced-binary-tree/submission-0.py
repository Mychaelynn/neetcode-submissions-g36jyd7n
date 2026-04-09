# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        #dfs 
        self.dfs(root)
        return self.balanced


    def dfs(self, root):
        
        if not root:
            return 0
        leftH = self.dfs(root.left) + 1
        rightH = self.dfs(root.right) + 1

        if abs(leftH-rightH)>1:
            self.balanced = False
        
        return max(leftH, rightH)
        