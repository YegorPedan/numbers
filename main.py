from itertools import product

digits = list(range(9, -1, -1))

operators = ['+', '-', '']

for combo in product(operators, repeat=9):
    expression = ''
    for i in range(9):
        expression += str(digits[i]) + combo[i]

    expression += str(digits[-1])

    result = eval(expression)

    if result == 200:
        print(expression, '=', result)