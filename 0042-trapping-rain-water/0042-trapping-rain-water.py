class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 1:
            return 0
        if len(height) == 2:
            return 0

        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
         
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        A = 0
        for i in range(1, len(height)-1):
            A +=  min(left[i], right[i]) - height[i]
        return A