
import code
w = code.Solution()

a = [-1,-2,-3]
matrix = [[0,19,54,9],[47,9,19,54],[11,47,9,19]]
cost = [10, 15, 20]
nums = [3,4,2,3]
nums1 = [4,2,1]
nums2 = [2,3,3,2,4]
M = [[1,1,1],
 [1,0,1],
 [1,1,1]]
#print(w.maximumProduct2(a))
#print(w.isToeplitzMatrix(matrix))
#print(len(matrix[1]))
#print(w.minCostClimbingStairs(cost))
#print(w.pivotIndex(nums))
#print(w.maxAreaOfIsland([[0,1,1,1,0,0,0,0]]))
#print(w.findLengthOfLCIS(nums))
#print(w.checkPossibility([1,2,3]))
print(w.imageSmoother(M))