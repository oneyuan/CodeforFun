#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        for i in s:
            if i == "(":
                left += 1
            elif i == ")":
                if left == 0:
                    right += 1
                if left > 0:
                    left -= 1

        res = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    res[ans] = 1
            else:
                if (s[index] == "(" and left_rem > 0) or (s[index] == ")" and right_rem > 0):
                    recurse(s, index+1, left_count, right_count, left_rem -
                            (s[index] == "("), right_rem-(s[index] == ")"), expr)
                expr.append(s[index])
                if s[index] != "(" and s[index] != ")":
                    recurse(s, index+1, left_count, right_count,
                            left_rem, right_rem, expr)
                elif s[index] == "(":
                    recurse(s, index + 1, left_count+1,
                            right_count, left_rem, right_rem, expr)
                elif s[index] == ")" and left_count > right_count:
                    recurse(s, index+1, left_count, right_count +
                            1, left_rem, right_rem, expr)
                expr.pop()

        recurse(s, 0, 0, 0, left, right, [])
        print(left, right)
        return list(res.keys())

    def removeInvalidParentheses0(self, s):
        """
        :type s: str
        :rtype: List[str]
        找所有res可以用dfs
        """
        rst = []
        self.dfs(s, 0, 0, '(', ')', rst)
        return rst

    def dfs(self, string, last_i, last_j, left, right, rst):

        cnt = 0

        for i in range(last_i, len(string)):
            if string[i] == left:
                cnt += 1
            elif string[i] == right:
                cnt -= 1
            if cnt < 0:
                for j in range(last_j, i+1):
                    if string[j] == right and (j == last_j or string[j-1] != right):
                        self.dfs(string[:j] + string[j+1:],
                                 i, j, left, right, rst)
                return

        str_rvs = string[::-1]
        if left == '(':
            self.dfs(str_rvs, 0, 0, right, left, rst)
        else:
            rst.append(str_rvs)

