class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1: return True
        pass_item = True

        # Check for first letter
        if ord(word[0]) < 91: capital = True
        else: capital = False

        if capital and ord(word[1]) > 90: capital = False

        for i, x in enumerate(word[1::]):
            
            if capital and ord(x) > 90: return False
            if not capital and ord(x) < 91: return False
            
        return pass_item
