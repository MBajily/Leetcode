# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        stack = []

        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        if stack == stack[::-1]:
            return True

        return False