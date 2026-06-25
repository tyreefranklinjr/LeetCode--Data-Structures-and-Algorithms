class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []; i = 0

        s = s.replace("-", "")
        
        for item in reversed(s):

            if i == k: result.insert(0, "-"); i = 0
            result.insert(0, item.upper())
            i += 1

        output = "".join(result)
        return output
