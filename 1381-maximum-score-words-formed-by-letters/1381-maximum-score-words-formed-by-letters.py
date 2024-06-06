class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def sol(n, letter):
            if n==len(words):
                return 0
            ans = 0
            copy=letter

            for i in words[n]:
                if i not in copy:
                    return sol(n+1, letter)
                copy = copy.replace(i, "", 1)
                ans+=score[ord(i)-97]

            return max(sol(n+1, letter), ans+sol(n+1, copy))
        return sol(0, "".join(letters))

                
                