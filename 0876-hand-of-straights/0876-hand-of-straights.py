class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        hand.sort()
        while hand !=[]:
            start = hand[0]
            hand.remove(start)
            for i in range(1, groupSize):
                if start+i not in hand:
                    return False
                else:
                    hand.remove(start+i)
        return True
        