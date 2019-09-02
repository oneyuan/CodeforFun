#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
import collections

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            return False

        def backTracking(s, path):
            if path == None:
                path = []
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    backTracking(s[i:], path+[s[:i]])

        res = []
        backTracking(s, None)
        return res

    def partition0(self, s: str) -> List[List[str]]:
        def make_results(index, pallindromes, result, results):
            if index >= len(s):
                results += result[:],
            else:
                for pallindrome in pallindromes[index]:
                    make_results(index + len(pallindrome),
                                 pallindromes, result + [pallindrome], results)

        n = len(s)
        is_pallindrome = set()
        pallindromes = collections.defaultdict(list)
        for i in range(0, len(s)):
            for j in range(i+1):
                if s[i] == s[j] and ((i-j) <= 1 or (j+1, i-1) in is_pallindrome):
                    is_pallindrome.add((j, i))
                    substring = s[j:i+1]
                    pallindromes[j] += substring,

        results = []
        make_results(0, pallindromes, [], results)
        return results
