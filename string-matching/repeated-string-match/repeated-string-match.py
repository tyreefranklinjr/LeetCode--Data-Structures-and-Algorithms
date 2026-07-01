class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        """a * a until b is in a"""
        i, x, t = 0, '', 0

        # a * a until >= len(b)
        while len(x) < len(b): i += 1; x = a * i

        # (a * a until >= len(b)) * 3
        while t <= 4:
            x = a * (i + t)
            if b in x: return i + t
            t += 1

        return -1
