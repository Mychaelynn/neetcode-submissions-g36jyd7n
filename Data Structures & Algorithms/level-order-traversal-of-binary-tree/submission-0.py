# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS - breadth first search

        # queue and FIFO

        res = []
        if not root:
            return res

        # Initialize the queue with  root node
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            
            # for every node in queue (every node on each level)
            for i in range(qLen):
                node = q.popleft() 
                
                # add children to queue for next while loop iteration 
                if node:
                    level.append(node.val) 
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
        
            if level:
                res.append(level)

        return res


        