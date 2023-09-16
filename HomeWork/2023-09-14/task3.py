# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while COUNT > 0:
    search_number = int(input('введите число- '))

    if search_number == num:
        print('Ура! Вы угадали')
        break
    elif search_number > num:
        print('Число меньше чем ваше')
        COUNT -= 1
        print(COUNT, 'осталось попыток')
    else:
        print('Число больше чем ваше')
        COUNT -= 1
        print(COUNT, 'осталось попыток')
else:
    print('Вы потратили все попытки')

