# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        stack = [(root,root.val)]

        while stack:
            node , curr_sum = stack.pop()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
            
            if node.left:
                stack.append((node.left , curr_sum + node.left.val))

            if node.right:
                stack.append((node.right , curr_sum + node.right.val))  
        return False     