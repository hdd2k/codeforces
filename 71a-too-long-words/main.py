
def shorten(s):
    if len(s) > 10:
        return s[0] + str(len(s) - 2) + s[-1]
    return s


lineNum = int(input())
# print(lineNum)
# while True:
for _ in range(lineNum):
    try:
        line = input()
        # print(f"line is : ({line})")
        # print(f"shortend line is : ({shorten(line)})")
        print(shorten(line))
    except EOFError:
        break

# print(lines)
