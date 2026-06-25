# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # pointing to the next no
            curr.next = prev
            prev = curr       #curr no will become the previous one
            curr = next_node  #moves to the next no
        return prev
        