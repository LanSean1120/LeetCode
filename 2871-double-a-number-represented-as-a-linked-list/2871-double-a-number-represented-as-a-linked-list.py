# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeval = []
        while head:
            nodeval.append(head.val)
            head = head.next
        
        
        
        nodeval = [2*val for val in nodeval]
        nodeval = nodeval[::-1]
        nodeval.append(0)


        for i in range(len(nodeval)-1):
            if nodeval[i] >=10:
                nodeval[i] %= 10
                nodeval[i+1] +=1

        nodeval = nodeval[::-1]

        if nodeval[0] == 0:
            nodeval = nodeval[1:len(nodeval)]
        
        head = ListNode(nodeval[0])
        current = head
        for val in nodeval[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
