class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.xs = defaultdict(set)
        self.ys = defaultdict(set)


    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.xs[x].add(y)
        self.ys[y].add(x)

    def count(self, point: List[int]) -> int:

        x, y = point
        res = 0

        for each_x in self.ys[y]:

            if each_x == x:
                continue
                
            x_diff = abs(x-each_x)

            for each_y in self.xs[x]:
                y_diff = abs(y-each_y)

                if y_diff != x_diff:
                    continue
                
                if self.points[(each_x, each_y)]:
                    print("entered", self.points, (x, y), (each_x, y), (x, each_y), (each_x, each_y))
                    res += self.points[(each_x, y)] * self.points[(x, each_y)] * self.points[(each_x, each_y)]
        
        return res
        
        