import fractions

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

num_1, num_2 = map(int, input().split('/'))
num_3, num_4 = map(int, input().split('/'))
numerator = num_1 * num_3
denominator = num_2 * num_4
result = ''
if num_1 == num_4:
    result = f'{num_3}/{num_2}'
    print(f'произведение равно {result}')
elif num_2 == num_3:
    result = f'{num_1}/{num_4}'
    print(f'произведение равно {result}')


elif denominator % numerator == 0:
    denominator = denominator // numerator
    numerator = 1
    print(f'произведение равно {numerator}/{denominator}')
else:
    print(f'произведение равно {numerator}/{denominator}')

if num_2 == num_4:
    sum_ = f'{num_1 + num_3}/{num_4}'
    print(f'сумма равна  {sum_}')
else:
    sum_ = f'{(num_1 * num_4) + (num_3 * num_2)}/{(num_2 * num_4)}'
    print(f'сумма равна  {sum_}')
