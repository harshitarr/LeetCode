# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        stack = []
        curr = root
        prev = None

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()


            if prev is not None and curr.val<=prev:
                return False

            prev = curr.val

            curr = curr.right
        return True
        