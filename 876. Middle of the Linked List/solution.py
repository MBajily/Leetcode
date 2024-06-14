# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head
        cur2 = head
        length = 0

        while cur:
            cur = cur.next
            length += 1

        for i in range(int(length/2)):
            cur2 = cur2.next
        
        return cur2