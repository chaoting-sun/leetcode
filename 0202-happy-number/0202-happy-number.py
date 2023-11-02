### method1: hash table

# time complexity: ?
# space complexity: O(N)

class Solution:
    def isHappy(self, n: int) -> bool:
        squares = [i**2 for i in range(10)]
        st = set()

        while n > 1:
            st.add(n)

            m = n
            cnt = 0
            while m > 0:
                m, mod = divmod(m, 10)
                cnt += squares[mod]
            n = cnt
            if cnt in st:
                return False
        return n == 1


### method1: fast and slow

# time complexity: ?
# space complexity: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:

        squares = [i**2 for i in range(10)]
        def computeSum(n):
            s = 0
            while n > 0:
                n, mod = divmod(n, 10)
                s += squares[mod]
            return s
        
        slow = fast = n

        while True:
            slow = computeSum(slow)
            fast = computeSum(fast)
            fast = computeSum(fast)
            
            if slow == 1 or slow == fast:
                break
        return slow == 1