import sys

for line in sys.stdin:
    if not line.lstrip().startswith('#'):
        sys.stdout.writelines(line)
