# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeval = []
        while head:
            nodeval.append(head.val)
            head = head.next
        sortval = [[] for k in range(len(nodeval)//k+1)]
        n=0
        for i in range(0,len(nodeval),k):
            if i+k>len(nodeval):
                sortval[n] = nodeval[i:]
                break
            sortval[n] = nodeval[i:i+k]
            sortval[n] = sortval[n][::-1]
            n+=1
        ansval = []
        for j in range(len(sortval)):
            ansval += sortval[j]
        ans = ListNode(ansval[0])
        current = ans
        for val in ansval[1:]:
            current.next = ListNode(val)
            current = current.next
        return ans
        