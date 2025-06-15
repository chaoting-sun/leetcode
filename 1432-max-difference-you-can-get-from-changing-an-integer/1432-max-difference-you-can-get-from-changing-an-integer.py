class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_num, min_num = num, num

        for digit in num_str:
            if digit != "9":
                max_num = int(num_str.replace(digit, "9"))
                break

        for i, digit in enumerate(num_str):
            if i == 0:
                if digit != "1":
                    min_num = int(num_str.replace(digit, "1"))
            else:
                if digit != num_str[0]:
                    candidate = int(num_str.replace(digit, "0"))
                    if candidate < min_num:
                        min_num = candidate

        return int(max_num) - int(min_num)