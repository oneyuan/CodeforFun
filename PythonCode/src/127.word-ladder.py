#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
import string
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        dic = {}
        for word in wordList:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                if key in dic:
                    dic[key].append(word)
                else:
                    dic[key] = [word]
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            cur, level = queue.popleft()
            for i in range(L):
                intm = cur[:i] + "*" + cur[i+1:]
                if intm in dic:
                    for word in dic[intm]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, level+1))
                    dic[intm] = []
        return 0

    def ladderLength0(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        if endWord == beginWord:
            return 1

        wordList.remove(endWord)
        head, tail = {beginWord}, {endWord}
        n, res = len(beginWord), 1

        while head and tail:
            if len(head) > len(tail):
                head, tail = tail, head
            next = set()
            while head:
                word = head.pop()
                for i in range(n):
                    prefix, suffix = word[:i], word[i+1:]
                    for c in string.ascii_lowercase:
                        candidate = prefix + c + suffix

                        if candidate in tail:
                            return res + 1
                        if candidate in wordList:
                            next.add(candidate)
                            wordList.remove(candidate)
            res += 1
            head = next

        return 0

