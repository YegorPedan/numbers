from itertools import product

digits = [str(x) for x in range(9, -1, -1)]
sings = ['+', '-', '']

for sign_comb in product(sings, repeat=9):
    expression = ''
    for index in range(9):
        expression += digits[index] + sign_comb[index]
    expression += '0'

    if eval(expression) == 200:
        print(f'{expression} = 200')