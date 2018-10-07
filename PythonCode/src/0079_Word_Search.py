import collections

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backTrack(word, i, x, y, board):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
                return False
            if board[x][y] != word[i]:
                return False
            board[x][y] = chr(ord(board[x][y]) ^ 256)
            boolean = backTrack(word, i+1, x+1, y, board) or backTrack(word, i+1, x, y+1, board) or backTrack(word, i+1, x-1, y, board) or backTrack(word, i+1, x, y-1, board)
            board[x][y] = chr(ord(board[x][y]) ^ 256)
            return boolean
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if backTrack(word, 0, x, y, board):
                    return True
        return False
    
    

    def dfs(self, board, i, j, word, k):
        # if we already checked all letters of the given word, return True
        if k == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        
        if board[i][j] == word[k]:
            # Prevent using the same element board[i][j] repeatedly, replace it with '#' 
            temp = board[i][j]
            board[i][j] = '#'
            # Recursively check each letter in its current adjacent cells
            res = self.dfs(board, i+1, j, word, k+1) or \
                self.dfs(board, i-1, j, word, k+1) or \
                self.dfs(board, i, j+1, word, k+1) or \
                self.dfs(board, i, j-1, word, k+1)
            board[i][j] = temp
            return res
        
        return False
   
    def exist0(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        # collections.Counter() returns a dict of the # of each elem
        # If some elem in word does not exist in board or there's more of it in word than in board, return False.
        board_c = collections.Counter([c for row in board for c in row])
        word_c = collections.Counter(word)
        for c in word_c:
            if not c in word_c or word_c[c] > board_c[c]:
                return False
            
        r, c = len(board), len(board[0])
        
        for i in range(r):
            for j in range(c):  
                if board[i][j] == word[0]:
                    res = self.dfs(board, i, j, word, 0)
                    if res:
                        return True
        
        return False

