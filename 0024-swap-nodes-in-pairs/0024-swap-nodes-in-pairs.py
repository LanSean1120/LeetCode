# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeval = []
        while head:
            nodeval.append(head.val)
            head = head.next
        for i in range(0,len(nodeval),2):
            if i == len(nodeval)-1:
                break
            nodeval[i], nodeval[i+1] = nodeval[i+1], nodeval[i]
        if nodeval == []:
            head = ListNode()
            return head.next
        ans = ListNode(nodeval[0])
        current = ans
        for val in nodeval[1:]:
            current.next = ListNode(val)
            current = current.next
        return ans