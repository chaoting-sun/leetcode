class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        newMat = [[0]*c for _ in range(r)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                order = i * n + j
                newMat[order//c][order%c] = mat[i][j]
        return newMat