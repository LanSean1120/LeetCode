# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodeval = [[]for i in range(len(lists))]
        for i in range(len(lists)):
            while lists[i]:
                nodeval[i].append(lists[i].val)
                lists[i] = lists[i].next
        ansval = []
        for i in range(len(nodeval)):
            for j in range(len(nodeval[i])):
                ansval.append(nodeval[i][j])
        ansval.sort()
        if ansval == []:
            head = ListNode()
            return head.next
        head = ListNode(ansval[0])
        current = head
        for val in ansval[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
        