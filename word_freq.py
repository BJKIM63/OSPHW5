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

rmdupli = set(words)
rmdupli = list(rmdupli)

count = dict()

for word_count in rmdupli:
    count[word_count] = words.count(word_count)

word_sorted = sorted(count.items(), key = lambda item: item[1], reverse = True)
print(word_sorted)

