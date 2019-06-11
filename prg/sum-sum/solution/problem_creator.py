import random
calc_len = 5000

random.seed(200)

expr = ""
for i in range(0, calc_len):
    expr += str(random.randint(10000, 20000))
    expr += f' + '

expr = expr[:-2]
print(expr)