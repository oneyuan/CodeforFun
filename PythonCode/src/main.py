
import code
w = code.Solution()

a = [-1,-2,-3]
matrix = [[0,19,54,9],[47,9,19,54],[11,47,9,19]]
cost = [10, 15, 20]
nums = [1, 0, -1, 0, -2, 2]
val = 0
k = 1
nums1 = [4,2,1]
nums2 = [2,3,3,2,4]
M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
flowerbed = [0,1,0]
n = 1
numbers = [1,2,3,4,4,9,56,90]
target = 0
s = "egg"
t = "add"
t = "2*3-4*5"
words = ["Hello","Alaska","Dad","Peace"]
buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
S = "ababcbacadefegdehijhklij"
num = "10200"
points = [[10,16], [2,8], [1,6], [7,12]]
strs = ["flower","flow","flight"]
digits = '23'
#print(w.maximumProduct2(a))
#print(w.isToeplitzMatrix(matrix))
#print(len(matrix[1]))
#print(w.minCostClimbingStairs(cost))
#print(w.pivotIndex(nums))
#print(w.maxAreaOfIsland([[0,1,1,1,0,0,0,0]]))
#print(w.maxSubArray(nums))
#print(w.findLengthOfLCIS(nums))
#print(w.checkPossibility([1,2,3]))
#print(w.imageSmoother(M))
#print(w.findMaxAverage(nums, k))
#print(w.canPlaceFlowers(flowerbed, n))
#print(w.findPairs(nums, k))
#print (w.missingNumber(nums))
#print(w.containsNearbyDuplicate(nums, k))
#print(w.rotate(nums, k))
#print(w.twoSum(numbers, target))
#print(w.removeElement(nums, val))
#print(w.twoSum(nums, target))
#print(w.maxArrayDC(nums))
#print(w.rob(nums))
#k = code.NumArray(nums)
#`print(k.sumRange(0, 5))
#print(w.firstBadVersion(10))
#print(w.isIsomorphic(s, t))
#print(w.diffWaysToCompute(t))
#print(w.findWords(words))
#print(w.getSkyline(buildings))
#print(w.partitionLabels(S))
#print(w.canJump(nums))
#print(w.getSkyline01(buildings))
#print(w.wiggleMaxLength(nums))
#print(w.removeKdigits(num, k))
#print(w.findMinArrowShots(points))
"""
print(zip(*strs))
for i,ch in enumerate(zip(*strs)):
    print (i, ch)
"""
#print(w.threeSum(nums))
#print(w.letterCombinations0(digits))
print(w.fourSum0(nums, target))