class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest = max(nums)

        for i in range(l):
            if i not in nums: return i

        return largest + 1

        # Time Complexity -> O(N) for elements in nums
        # Space Complexity -> O(1) as the auxillary space remains constant
