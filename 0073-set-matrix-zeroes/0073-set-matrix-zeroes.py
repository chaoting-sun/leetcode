### mark those that needs to be 0

# time complexity: O(mn)
# space complexity: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # horizontal line
                    j1, j2 = j-1, j+1
                    while j1 >= 0 and matrix[i][j1] != 0:
                        matrix[i][j1] = '#'
                        j1 -= 1
                    while j2 < n and matrix[i][j2] != 0:
                        matrix[i][j2] = '#'
                        j2 += 1

                    # vertical line
                    i1, i2 = i-1, i+1
                    while i1 >= 0 and matrix[i1][j] != 0:
                        matrix[i1][j] = '#'
                        i1 -= 1
                    while i2 < m and matrix[i2][j] != 0:
                        matrix[i2][j] = '#'
                        i2 += 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0


### store the rows/cols that needs to be 0

# time complexity: O(mn)
# space complexity: O(log(m+n))

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0


### in-table hashing - we use the first row and first column to remember if the row or column should be 0.

# time complexity: O(mn)
# space complexity: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowIs0, firstColIs0 = False, False

        for j in range(n):
            if matrix[0][j] == 0:
                firstRowIs0 = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstColIs0 = True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstRowIs0:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstColIs0:
            for i in range(m):
                matrix[i][0] = 0