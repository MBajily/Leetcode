# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        cur = head
        unique = set()
        while cur:
            if cur not in unique:
                unique.add(cur)
                cur = cur.next
            
            else:
                return True
        
        return False