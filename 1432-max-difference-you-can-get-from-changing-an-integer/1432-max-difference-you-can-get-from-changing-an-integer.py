class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        a = num
        for digit in num_str:
            candidate = int(num_str.replace(digit, "9"))
            a = max(a, candidate)

        b = num
        for index, digit in enumerate(num_str):
            if index != 0 and num_str[0] != digit:
                candidate = int(num_str.replace(digit, "0"))
                if candidate != 0:
                    b = min(b, candidate)

            candidate = int(num_str.replace(digit, "1"))
            b = min(b, candidate)
        
        return a - b

