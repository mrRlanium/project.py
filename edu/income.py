import sys

income = int(sys.argv[1])
tax = int(sys.argv[2])

income_tax = income - (income * (tax / 100))
print(round(income_tax, 2))
