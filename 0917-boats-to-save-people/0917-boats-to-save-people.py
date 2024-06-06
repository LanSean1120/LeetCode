class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        start, end = 0, len(people)-1
        ans = 0
        while start<=end:
            if people[end]+people[start]<=limit:
                ans +=1
                start+=1
                end-=1
            else:
                ans+=1
                end-=1
        return ans
        