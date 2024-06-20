# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = head
        cur = head
        prev = head

        if cur == prev and cur != None:
            cur = cur.next
        
        while cur:
            if cur.val == prev.val:
                cur = cur.next
                if cur == None:
                    prev.next = None
            else:
                prev.next = cur
                cur = cur.next
                prev = prev.next

        return d
        