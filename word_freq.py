#!/usr/bin/python3
import string
import sys
args = sys.argv[1:]
fpin = open(args[0], "r")

words = list()

while 1:
    line = fpin.readline()
    if not line:
        break
    clearline = line.translate(str.maketrans('','',string.punctuation))
    words += clearline.split()

rmdupli = set(words)
rmdupli = list(rmdupli)

count = dict()

for word_count in rmdupli:
    count[word_count] = words.count(word_count)

word_sorted = sorted(count.items(), key = lambda item: item[1], reverse = True)

for i in range(int(args[1])):
    print("%-10s %5d" %(word_sorted[i][0], word_sorted[i][1]))
