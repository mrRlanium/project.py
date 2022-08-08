import sys

number = sys.argv[1]

print('+7', '('+number[1:4]+')', number[4:7]+'-'+number[7:9]+'-'+number[-2:])
print('+7', '('+number[1:4]+')', end=' ')
print(number[4:7], number[7:9], number[-2:], sep='-')