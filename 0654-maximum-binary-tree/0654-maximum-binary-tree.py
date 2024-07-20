# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def sol(l):
            if l==[]:
                return
            if len(l) == 1:
                return TreeNode(l[0])
            Node = TreeNode()
            maxx = 0
            for i in range(len(l)):
                if l[i] > l[maxx]:
                    maxx = i
            Node.val = l[maxx]
            Node.left = sol(l[:maxx])
            Node.right = sol(l[maxx+1:])
            return Node
        return sol(nums)

