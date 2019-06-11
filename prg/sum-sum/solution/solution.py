number = open('../participants/numbers.txt', 'r')


expr = number.read()
print(eval(expr))