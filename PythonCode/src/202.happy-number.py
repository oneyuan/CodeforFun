#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        re = []
        tmp = 0
        while tmp not in re:
            re.append(n)
            string = str(n)
            tmp = 0
            for i in string:
                tmp += pow(int(i), 2)
            if tmp == 1:
                return True
            n = tmp
        return False

    def isHappy0(self, n: int) -> bool:
        dictionary = {}
        sum_of_squares = 0
        while sum_of_squares != 1:
            sum_of_squares = 0
            for i in str(n):
                sum_of_squares += int(i)**2
            n = sum_of_squares
            if n not in dictionary:
                dictionary[n] = 1
            else:
                return False
        return True

