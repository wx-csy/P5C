#!/usr/bin/python3
import sys, random
random.seed(int(sys.argv[1]))
print(*[random.randint(0, 100) for i in (0,0)])
