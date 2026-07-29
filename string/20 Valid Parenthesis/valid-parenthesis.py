class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:

            if ch in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[ch] != top_element:
                    return False
            else: stack.append(ch)

        return not stack

        # Time Complexity -> O(N) as n is the length of s
        # Space Complexity -> O(1) as the auzillary space is constant
