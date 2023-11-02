class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.x2p = defaultdict(set)
        self.y2p = defaultdict(set)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.freq[point] += 1
        self.x2p[point[0]].add(point)
        self.y2p[point[1]].add(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0

        for px, py in self.x2p[x]:
            # overlap
            if y == py:
                continue
            
            width = abs(py-y)
            p1, p2 = (x-width, y), (x+width, y)

            if p1 in self.freq and (p1[0],py) in self.freq:
                cnt += self.freq[p1] * self.freq[(px,py)] * self.freq[(p1[0],py)]

        return cnt


class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0

        for px, py in self.freq:
            if px - x == 0 or py - y == 0 or abs(px-x) != abs(py-y):
                continue
            if (px, y) in self.freq and (x, py) in self.freq:
                cnt += self.freq[(px, py)] * self.freq[(px, y)] * self.freq[(x, py)]
        return cnt


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)