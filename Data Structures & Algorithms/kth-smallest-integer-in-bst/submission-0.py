# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # go theoug the whole list

        res = []
        self.helper(root, res)

        res.sort()

        return res[k-1]

    
    def helper(self,root, res):

        if not root:
            return

        
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right,res)
        