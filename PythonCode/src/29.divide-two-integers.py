#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        sign = 1 if (dividend > 0) == (divisor > 0) else -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        multiples = []
        a = divisor
        while a <= dividend:
            multiples.insert(0, a)
            a += a

        string = '0'
        for m in multiples:
            if dividend >= m:
                string += '1'
                dividend -= m
            else:
                string += '0'

        max_int = 2 ** 31
        quotient = int(string, 2)
        if sign > 0 and quotient >= max_int:
            return max_int - 1
        if sign < 0 and quotient > max_int:
            return max_int - 1

        return quotient * sign

