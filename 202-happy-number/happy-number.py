class Solution(object):
    def isHappy(self, n):
        if n == 1 or n == 7:
            return True

        if n < 10:
            return False

        summ = 0

        while n > 0:
            digit = n % 10
            summ += digit ** 2
            n //= 10

        return self.isHappy(summ)