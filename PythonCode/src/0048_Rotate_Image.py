class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        print(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        #Consider each square, there are n/2 of them
        N = len(matrix[0])
        for x in range(0, int(N/2)):
            #For each group of four in the current square
            for y in range(x, N-x-1):
                # store bottom left cell in temp variable
                temp = matrix[N-1-y][x]
                # move values from bottom right to bottom left
                matrix[N-1-y][x] = matrix[N-1-x][N-1-y]                
                # move values from top right to bottom right 
                matrix[N-1-x][N-1-y] = matrix[y][N-1-x] 
                # move values from top left to top right
                matrix[y][N-1-x] = matrix[x][y]
                # assign temp to top left
                matrix[x][y] = temp
    
    def rotate0(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(l):
            for j in range(l//2):
                matrix[i][j], matrix[i][l-j-1] = matrix[i][l-j-1], matrix[i][j]