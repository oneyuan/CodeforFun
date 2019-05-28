#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.97%)
# Likes:    582
# Dislikes: 1707
# Total Accepted:    354.8K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            while not s[i].isalnum():
                if i >= n-1:
                    return True
                i += 1
            while not s[j].isalnum():
                if j < 1:
                    return True
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome0(self, s: str) -> bool:
        s=s.translate(s.maketrans('','',string.punctuation))
        s=s.lower().replace(' ','')
        return (s==s[::-1])

