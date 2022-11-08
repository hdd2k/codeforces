

# read input

def Graph():
    def __init__(self, lineContents):
        self.graph = []
        # for

    def __repr__(self):
        finalStr = "########\n"
        for row in self.graph:
            for col in row:
                finalStr += str(col)
            finalStr += "\n"
        finalStr += "########"
        return finalStr

    def findOnePos():
        pass

    def findDist():
        pass

        # finalStr = "\n"
        # for i, numList in enumerate(self.boardlines):
        #     for j, num in enumerate(numList):
        #         finalStr += f"{str(num)}[{self.boardcalled[i][j]}]" + " "
        #     finalStr += "\n"
        # return finalStr


# Problem
# Find min transformations to input matrix to be beautiful.
# "beautiful" -> the single "1" is in middle
# Transformations:
# - swap 2 adjacent rows
# - swap 2 adjacent cols


# Solution
# 1. Find the "1" in the matrix
# 2. Find distance from middle, and add to total.
