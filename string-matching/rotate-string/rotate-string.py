class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """Rotate s, n times until s == goal, else return False"""

        i = 0

        # Check for match until we surpass relevant uses
        while (i := i + 1) <= len(s):

            # Rotate the string
            tmp = list(s)
            ch = tmp.pop(0); tmp.append(ch)

            # Check for match
            s = "".join(tmp)
            if s == goal: return True
    
        return False
