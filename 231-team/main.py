

# parse stdin
# 1 line -> how many lines to read
# each line -> 3 str of ints that tell you who knows
# solve if 2+ 1's -> true

lineCount = int(input())

totalSolvable = 0
for _ in range(lineCount):
    line = input()
    splitLine = [int(s) for s in line.split(" ")]
    if sum(splitLine) >= 2:
        totalSolvable += 1

print(totalSolvable)
