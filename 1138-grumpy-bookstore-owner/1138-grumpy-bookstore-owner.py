class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes == len(customers):
            return sum(customers)

        grumpy_customers = [customers[i]*grumpy[i] for i in range(len(grumpy))]

        tech = [sum(grumpy_customers[i:i+minutes]) for i in range(len(grumpy)-minutes+1)]
        optimal = max(tech)
        res = sum(customers) - sum(grumpy_customers)
        return res + optimal