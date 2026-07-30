class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        There are brute force options that allow you to
        sort through each iteration respectively. This 
        has a poor runtime relative to peeking. Therefore,
        this coding solution utilizes a hashmap to grab
        complementary value quicker and return the
        corresponding index.
        """

        seen = {}
        # {number: index}

        for index, num in enumerate(nums):
            
            complementary = target - num

            if complementary in seen:
                return [seen[complementary], index]

            seen[num] = index

        # Time Complexity -> O(N) as n is the number of elements in n
        # Space Complexity -> O(1) as the auxillary data remains constant
