import sys

k: int = 0

for line in sys.stdin:
    if line.lstrip().startswith('#'):
        k += 1
else:
    print(k)
