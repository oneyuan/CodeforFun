# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n < 1:
            return None
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def sortedArrayToBST0(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None

        return self.toBstUtil(nums, 0, len(nums) - 1)

    def toBstUtil(self, nums, low, high):

        if low > high:
            return None

        mid = (low + high) // 2

        node = TreeNode(nums[mid])
        node.left = self.toBstUtil(nums, low, mid - 1)
        node.right = self.toBstUtil(nums, mid + 1, high)

        return node
