class Solution:
    def isHappy(self, n: int) -> bool:
        squares = [i**2 for i in range(10)]
        st = set()

        while n >= 4:
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