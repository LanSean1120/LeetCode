class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deck = deque(deck)
        ans = deque()
        while deck:
            if ans:
                temp = ans.pop()
                ans.appendleft(temp)
                curr = deck.pop()
                ans.appendleft(curr)
            else:
                curr = deck.pop()
                ans.append(curr)
        return list(ans)


        return ans

