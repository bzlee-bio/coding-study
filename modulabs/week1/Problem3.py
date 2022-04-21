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
        pTempHead = ListNode(-1, head)
        
        pStart = pTempHead
        
        
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                pStart.next = head.next
            else:
                pStart = pStart.next
            head = head.next
                
            
            

        return pTempHead.next