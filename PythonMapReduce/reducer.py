import sys

currentWord = None
currentCount = 0
word = None

for line in sys.stdin:
    word, count = line.split("\t",1)
    
    count = int(count)
    if word == currentWord:
        currentCount += count
    else:
        if currentWord:
            print(currentWord,"\t",currentCount)
        currentWord = word
        currentCount = count

if currentWord == word:
    print(currentWord,"\t",currentCount)
