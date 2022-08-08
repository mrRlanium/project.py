import sys

word = sys.argv[1]
print('', '-' * (len(word) + 2), sep='+', end='+\n')
print('|', word, end=' |\n')
print('', '-' * (len(word) + 2), sep='+', end='+\n')
