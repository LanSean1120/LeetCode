# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodeval = []
        while head:
            nodeval.append(head.val)
            head = head.next
        nodeval.pop(len(nodeval)-n)
        ansval = nodeval
        if ansval == []:
            head = ListNode()
            return head.next
            
        head = ListNode(ansval[0])
        current = head
        for val in ansval[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
