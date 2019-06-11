import random
flag = "STRT{pick_up_the_pieces}"
str_len = 500000
random.seed(1928)

expr = ""
pad = "!"
iterator = iter(flag)

for i in range(0, str_len):
    expr += pad
    try:
        if random.random() < 1/(str_len/len(flag)):
            expr += next(iterator)
    except:
        expr += pad

print(expr)