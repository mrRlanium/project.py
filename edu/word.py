import sys

word = sys.argv[1]
if len(word) % 2 == 0:
    print(word[int(len(word) / 2 - 1)])
else:
    print(word[int(len(word) / 2)])
