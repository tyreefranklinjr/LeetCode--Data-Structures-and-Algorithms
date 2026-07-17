class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums); l = 0
        
        for i, x in enumerate(nums):
            if x - 1 not in nums:
                le = 0
                while x + le in nums: le += 1
                l = max(l, le)
        return l
