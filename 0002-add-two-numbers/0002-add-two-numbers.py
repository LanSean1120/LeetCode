# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        li1 = []
        current1 = l1
        while current1:
            li1.append(current1.val)
            current1 = current1.next
        li2 = []
        current2 = l2
        while current2:
            li2.append(current2.val)
            current2 = current2.next

        
        ln1 = 0
        for i in range(len(li1)):
            ln1+=li1[i]*10**i

        ln2 = 0
        for i in range(len(li2)):
            ln2+=li2[i]*10**i

        ln3=str(ln1+ln2)
        ln3 = ln3[::-1]
        ans = []
        for i in range(len(ln3)):
            ans.append(int(ln3[i]))

        
        def list_to_listnode(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for val in lst[1:]:
                current.next = ListNode(val)
                current = current.next
            return head

        return list_to_listnode(ans)

                
        

        