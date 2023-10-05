class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        nRows, nCols = len(matrix), len(matrix[0])
        nEle = nRows * nCols
        upRight, downRight, downLeft, upLeft = nCols, nRows, -1, -1

        ans = [matrix[0][0]]
        i = 0
        j = 1

        while True:
            while j < upRight:
                ans.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1            
            upLeft += 1

            if len(ans) == nEle:
                break

            while i < downRight:
                ans.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            upRight -= 1


            if len(ans) == nEle:
                break

            while j > downLeft:
                ans.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            downRight -= 1

            if len(ans) == nEle:
                break

            while i > upLeft:
                ans.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            downLeft += 1

            if len(ans) == nEle:
                break
        return ans