# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.



number = int(input("введите число "))
print("Встроеная  функция", hex(number))

sixteen_system = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
res = ''
while number:
    res = sixteen_system[number % 16] + res
    number = number // 16

print('0x' + res)
