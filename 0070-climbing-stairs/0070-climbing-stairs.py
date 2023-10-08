### method1: divide and conquer (TLE)

# class Solution:
#     def climb(self, curr, n):
#         if curr == n:
#             return 1
        
#         n1 = n2 = 0
#         if curr + 1 <= n:
#             n1 = self.climb(curr+1, n)
#         if curr + 2 <= n:
#             n2 = self.climb(curr+2, n)
#         return n1 + n2        

#     def climbStairs(self, n: int) -> int:
#         return self.climb(0, n)


### method2: Fibonacci sequence

class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0 for _ in range(n)]

        if n == 1:
            return 1
        elif n == 2:
            return 2

        fib[0], fib[1] = 1, 2
        for i in range(2, n):
            fib[i] = fib[i-2] + fib[i-1]
        return fib[n-1]
