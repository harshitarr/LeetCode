class Solution(object):
    def maximumWealth(self, accounts):
        max_money = 0

        for customer in accounts:
            wealth = sum(customer)
            max_money = max(max_money , wealth)
        return max_money

        