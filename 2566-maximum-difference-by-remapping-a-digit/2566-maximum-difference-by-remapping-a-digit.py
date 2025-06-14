class Solution:
    def minMaxDifference(self, num: int) -> int:
        if num < 10:
            return 9 - 0

        temp_num = num

        new_digit_for_large = 9
        new_digit_for_small = 9
        
        
        while True:
            remain = temp_num % 10
            temp_num = (temp_num - remain) // 10
            if remain != 9:
                new_digit_for_large = remain
            if temp_num == 0:
                new_digit_for_small = remain
                break

        temp_num = num
        smallest_num = 0
        largest_num = 0
        count = 0

        while True:
            remain = temp_num % 10
            if remain == new_digit_for_large:
                largest_num += 9 * 10**count
            else:
                largest_num += remain * 10**count 
            if remain != new_digit_for_small:
                smallest_num += remain * 10**count

            temp_num = (temp_num - remain) // 10
            count += 1
            if temp_num == 0:
                break
        
        return largest_num - smallest_num
