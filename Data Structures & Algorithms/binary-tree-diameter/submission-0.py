# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  

    # get max from left and righta and add

    # def helperDia (root):

    #     if not root:
    #         return None
        
    #     left =1+self.helperDia(root.left)
    #     right =  1+self.helperDia(root.right)

    #     maxSIde = max(left,right)

    #     maxAll = max (left+right, )


    # space complexiity is porpotional to height
    # O(logn) for balanced and O(n)
################################################################

        self.result = 0


        #returns height
        def dfs(curr):
            if not curr:
                return 0
            
            left=dfs(curr.left)
            right=dfs(curr.right)
            
            self.result = max(self.result, left+right)

            return max(left,right) + 1
        
        dfs(root)
        return self.result

        


        