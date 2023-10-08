### method1: divide and conquer (O(2^n); TLE)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0 or n == 1:
#             return 1
#         return self.climbStairs(n-2) + self.climbStairs(n-1)


### method2: Fibonacci sequence

class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0 for _ in range(n)]

        if n == 1 or n == 2:
            return n
        
        fib[0], fib[1] = 1, 2
        for i in range(2, n):
            fib[i] = fib[i-2] + fib[i-1]
        return fib[n-1]
