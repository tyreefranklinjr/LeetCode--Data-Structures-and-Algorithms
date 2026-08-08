class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """
        There are brute force options to easily
        sort through this list repeatedl, however
        with respects to big(o) notation, we can
        use a depth-first search algorithm tied
        with hashmaps for the mapped digits to properly
        form a quick sort of the output.
        """
        
        lib = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        
        def dfs_recursive(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
                
            for char in lib[digits[i]]:
                dfs_recursive(i + 1, currStr + char)
                
                
        if digits: dfs_recursive(0, "")
        
        return res
        
        # Time Complexity -> O(4^n * N) as N is the number of elements in digits
        # Space Complexity -> O(1) as the auxillary space remains constant
