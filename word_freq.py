#!/usr/bin/python3
import string
fpin = open("article.txt", "r")

words = list()

while 1:
    line = fpin.readline()
    if not line:
        break
    clearline = line.translate(str.maketrans('','',string.punctuation))
    words += clearline.split()

print(words)
