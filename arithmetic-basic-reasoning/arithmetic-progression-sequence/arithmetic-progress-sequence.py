class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort(); prev = abs(arr[0] - arr[1])
        while len(arr) > 1:
            c = abs(arr[0] - arr[1])
            if c != prev: return False
            arr.pop(0); prev = c
        
        return True
