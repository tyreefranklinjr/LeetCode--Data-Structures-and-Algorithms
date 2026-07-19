class Solution:
    def longestPalindrome(self, s: str) -> str:

        re = ""
        rLen = 0
        for i in range(len(s)):
            l, r = i, i

            # Odd Subs
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rLen:
                    re = s[l:r + 1]
                    rLen = r - l + 1
                l -= 1; r += 1
            
            l, r = i, i + 1
            # Even Subs
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rLen:
                    re = s[l:r + 1]
                    rLen = r - l + 1

                l -= 1; r += 1

        return re
