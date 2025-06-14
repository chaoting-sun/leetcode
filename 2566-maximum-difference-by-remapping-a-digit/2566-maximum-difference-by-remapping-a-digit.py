class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        max_val = num
        for digit in num_str:
            if digit != "9":
                max_val = int(num_str.replace(digit, "9"))
                break
        min_val = int(num_str.replace(num_str[0], "0"))
        return max_val - min_val