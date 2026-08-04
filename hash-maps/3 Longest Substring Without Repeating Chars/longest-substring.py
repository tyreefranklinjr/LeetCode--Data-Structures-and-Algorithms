class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The solution can easily be brute forced with two
        pointer while loops, however for optimized search,
        I utilized a 'seen' hash map connected to a sliding
        window that can find the longest substring in
        one interation of the 's' string.
        """
        l = 0
        longest = 0
        seen = {}
        # {char: index}

        for r, ch in enumerate(s):
        
            if ch in seen and seen[ch] >= l:
                l = seen[ch] + 1

            seen[ch] = r
            longest = max(longest, r - l + 1)
                
        return longest

        # Time Complexity -> O(N) as n is the number of elements in s
        # Space Complexity -> O(1) as all auxillary space remains constant
