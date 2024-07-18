class Solution:
    def numberToWords(self, num: int) -> str:
        
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        if num == 0:
            return d[0]
        ans = ""
        B = num//1000000000
        if B!=0:
            if B//100 !=0:
                ans += d[B//100] + " " + d[100] + " "
                B%=100
            if B//10 == 1:
                ans += d[B] + " "
                B = 0
            if B//10 != 0:
                ans += d[B//10 *10] + " "
                B %= 10
            if B != 0:
                ans += d[B] + " "
            ans+=d[1000000000] +" "
        num %= 1000000000

        M = num//1000000
        if M!=0:
            if M//100 !=0:
                ans += d[M//100] + " " + d[100] + " "
                M%=100
            if M//10 == 1:
                ans += d[M] + " "
                M = 0
            if M//10 != 0:
                ans += d[M//10 *10] + " "
                M %= 10
            if M != 0:
                ans += d[M] + " "
            ans+=d[1000000] +" "
        num %= 1000000

        t = num//1000
        if t!=0:
            if t//100 !=0:
                ans += d[t//100] + " " + d[100] + " "
                t%=100
            if t//10==1:
                ans += d[t] + " "
                t = 0
            if t//10 != 0:
                ans += d[t//10 *10] + " "
                t %= 10
            if t != 0:
                ans += d[t] + " "
            ans+=d[1000] +" "
        num %= 1000
        
        if num//100 !=0:
            ans += d[num//100] + " " + d[100] + " "
            num %=100
        if num//10 == 1:
            ans+=d[num]+" "
            num=0
        if num//10 !=0:
            ans += d[num//10 *10] + " "
            num %= 10
        if num !=0:
            ans += d[num] + " "
        return ans[:len(ans)-1]
        





