class Solution:
    def intToRoman(self, num: int) -> str:

        """
        Placed all valid test cases in the lib hashmap,
        then validated them by running an inverse loop
        to check if there are any valid uses for each 
        hash to be used on the num, returned the roman
        numerical output.
        """

        lib = [
            [1, "I"],
            [4, "IV"],
            [5, "V"],
            [9, "IX"],
            [10, "X"],
            [40, "XL"],
            [50, "L"],
            [90, "XC"],
            [100, "C"],
            [400, "CD"],
            [500, "D"],
            [900, "CM"],
            [1000, "M"],
        ]

        res = ""

        for val, s in reversed(lib):
            if num // val: 
                count = num // val
                res += s * count
                num -= val * count

        return res

    # Time Complexity -> O(N) as n is the number of elements in lib
    # Space Complexity O(1) as all auxillary spaces remain constant
