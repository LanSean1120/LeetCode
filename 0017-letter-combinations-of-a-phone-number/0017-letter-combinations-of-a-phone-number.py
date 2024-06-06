class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for i in range(len(digits)):
            num = int(digits[i])-2
            ans = [a+b for a in ans for b in letters[num]]
        return ans if ans != [""] else []
