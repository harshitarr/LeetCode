# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        stack = [(p,q)]

        while stack:
            root1,root2 = stack.pop()

            if not root1 and not root2:
                continue

            if not root1 or not root2:
                return False
            
            if root1.val!=root2.val:
                return False
            
            stack.append((root1.left,root2.left))
            stack.append((root1.right,root2.right))

        return True


        
        