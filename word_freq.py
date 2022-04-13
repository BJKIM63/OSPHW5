#!/usr/bin/python3
import string
fpin = open("article.txt", "r")

words = list()

while 1:
    line = fpin.readline()
    if not line:
        break
    words += line.split()

print(words)
