

# read input

class Graph():
    def __init__(self, lines):
        self.graph = []
        for l in lines:
            self.graph.append(l.split(" "))

    def __repr__(self):
        finalStr = "########\n"
        for row in self.graph:
            for col in row:
                finalStr += str(col)
            finalStr += "\n"
        finalStr += "########"
        return finalStr

    def findOnePos(self):
        for rIdx, row in enumerate(self.graph):
            for cIdx, col in enumerate(row):
                if col == "1":
                    return cIdx, rIdx

    def findDist(self):
        onePos = self.findOnePos()
        return (abs(onePos[0] - 2) + abs(onePos[1] - 2))

# Problem
# Find min transformations to input matrix to be beautiful.
# "beautiful" -> the single "1" is in middle
# Transformations:
# - swap 2 adjacent rows
# - swap 2 adjacent cols


# Solution
# 1. Find the "1" in the matrix
# 2. Find distance from middle, and add to total.
lines = []
try:
    while True:
        lines.append(input())
except Exception as e:
    pass
    # print(f"End of line")
# print(lines)

g = Graph(lines)
print(g.findDist())
