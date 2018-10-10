class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        count = [0 for _ in range(26)]
        if s1 == s2:
            return True
        
        for i in range(n):
            count[ord(s1[i]) - ord("a")] += 1
            count[ord(s2[i]) - ord("a")] -= 1
        
        for i in range(26):
            if count[i] != 0:
                return False
        
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
        
        return False

    def isScramble0(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def Iter(p1, p2, N):
        	if N <= 3:
        		return True
        	s1_left = [0 for i in range(26)]
        	s1_right = [0 for i in range(26)]
        	s2_left = [0 for i in range(26)]
        	s2_right = [0 for i in range(26)]

        	for l in range(N//2):
        		N_ = l + 1
        		s1_left[ord(s1[p1 + l]) - ord('a')] += 1
        		s2_left[ord(s2[p2 + l]) - ord('a')] += 1
        		s1_right[ord(s1[p1 + N - l - 1]) - ord('a')] += 1
        		s2_right[ord(s2[p2 + N - l - 1]) - ord('a')] += 1

        		if s1_left == s2_left and Iter(p1, p2, N_) and Iter(p1 + N_, p2 + N_, N - N_):
        			return True
        		if s1_left == s2_right and Iter(p1, p2 + N - N_, N_) and Iter(p1 + N_, p2 , N - N_):
        			return True
        		if s1_right == s2_left and Iter(p1 + N - N_, p2, N_) and Iter(p1, p2 + N_, N - N_):
        			return	True
        		if s1_right == s2_right and Iter(p1 + N - N_, p2 + N - N_, N_) and Iter(p1, p2 , N - N_):
        			return True
        	return False
        Ds1 = [0 for i in range(26)]
        Ds2 = [0 for i in range(26)]
        for c1, c2 in zip(s1, s2):
        	Ds1[ord(c1) - ord('a')] += 1
        	Ds2[ord(c2) - ord('a')] += 1
        if Ds1 != Ds2:
        	return False
        return Iter(0, 0, len(s1))