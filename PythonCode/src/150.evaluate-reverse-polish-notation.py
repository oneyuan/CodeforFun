#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        n = len(tokens)
        operators = ["+", "-", "*", "/"]
        res = []
        for i in range(n):
            if tokens[i] not in operators:
                res.append(int(tokens[i]))
            else:
                second = res.pop()
                first = res.pop()
                if tokens[i] == "+":
                    res.append(first + second)
                elif tokens[i] == "-":
                    res.append(first - second)
                elif tokens[i] == "*":
                    res.append(first * second)
                elif tokens[i] == "/":
                    res.append(int(first / second))
        if len(res) == 1:
            return res[0]
        else:
            return 0


