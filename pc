#!/usr/bin/env python3
import sys
import bin as mainprog

if __name__ == "__main__" :
    args = sys.argv
    if len(args) < 2 :
        exit(1)
    mainprog.main(*args[1:])
