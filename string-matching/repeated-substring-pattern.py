class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Determines if an string can be constructed by repeating a substring."""
        hlf_i = len(s) // 2
        hlf_str = s[:hlf_i]

        # Iterates through all possible substrings in s[:s // 2]
        for i, char in enumerate(hlf_str):

            substr = s[0:i + 1]

            # Check if the substring is accurate by repeating the phrase cts times
            cts = len(s) // len(substr)
            if substr * cts == s: return True

        return False
