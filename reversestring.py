import sys
def rev(string):
    return string[::-1]

for line in sys.stdin:
    print rev(str(line))