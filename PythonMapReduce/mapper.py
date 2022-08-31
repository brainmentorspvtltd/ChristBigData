import sys

data = sys.argv[1]
# print(data)
words = data.split(",")
for word in words:
    print(word+"\t"+"1")
