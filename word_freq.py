#!/usr/bin/python3
import string
fpin = open("article.txt", "r")

while 1:
    line = fpin.readline()
    if not line:
        break
    print(line)
