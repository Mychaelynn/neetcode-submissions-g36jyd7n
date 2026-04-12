# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS


        # calculate the depth of each node
    #     if root is None:
    #         return 0


    #     height = 1
    #     res = []

    #     if root.val>=1:
    #         res.append(root.val)

    #     while root:
        
    #         # Safer version
    #         if root.left and self.calHeight(root.left, height + 1):
    #             res.append(root.left.val)
    #         # Safer version
    #         if root.right and self.calHeight(root.right, height + 1):
    #             res.append(root.right.val)
    #     return len(res)

    # def calHeight(self, node, level):
    #     if node.val>=level:
    #         return False
    #     return True

    

        if not root:
            return 0

        return self.helper(root, root.val)
        
        
    

    def helper(self, node, maxx):
        if not node:
            return 0
        
        count = 0
        if node.val>=maxx:
            count=1
            maxx=node.val
        count+= self.helper(node.left,maxx)
        count+= self.helper(node.right,maxx)
        return count



        