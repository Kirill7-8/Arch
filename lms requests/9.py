import sys
print({x.split("=")[0]: x.split("=")[1].strip() for x in sys.stdin})