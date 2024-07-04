# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_l = []
        count = 0
        while(head!=None):
            if head.val == 0 and count>0:
                ans_l.append(count)
                count = 0
            else:
                count += head.val
            head = head.next
        ans_l = ans_l[::-1]
        ans = None
        for i in range(len(ans_l)):
            ans = ListNode(ans_l[i], ans)
        return ans
       

                
            