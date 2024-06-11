class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {i:j for j, i in enumerate(arr2)}
        def func(x,y):
            if x in d and y in d:
                if d[x]>=d[y]:
                    return 1
                else:
                    return -1
            elif x in d:
                return -1
            elif y in d:
                return 1
            else:
                if x>=y:
                    return 1
                else:
                    return -1
        arr1.sort(key = cmp_to_key(func))    
        return arr1