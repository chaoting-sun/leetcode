class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        startColor = image[sr][sc]
        visited = [[False for _ in range(n)] for _ in range(m)]

        while q:
            size = len(q)

            for i in range(size):
                x, y = q.popleft()
                image[x][y] = color
                visited[x][y] = True
                
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newx, newy = x + dx, y + dy
                    if not 0 <= newx < m or not 0 <= newy < n:
                        continue
                    if not visited[newx][newy] and image[newx][newy] == startColor:
                        q.append((newx, newy))
        return image