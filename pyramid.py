#!/usr/bin/python
# -*- coding: utf-8 -*-

#pyramid.py
def returnAster(count):
    ret = ""
    for i in range(count):
        for j in range(i+1):
            ret += "*"
        ret += "\n"
    ret = ret[:-1]
    return ret

if __name__ == "__main__":
    for i in range(5):
        print returnAster(i)
        print "\n"
