#!/usr/bin/env python

# Оператор if (обязательный). else-блок - не обязательный
num = 23
# int - класс. Служит для преобразования строк в целые числа
# guess = int(input('Enter a number : '))
# if guess == num:
#     print('Congrats! You are right!')
# elif guess < num:
#     print('Wrong. The number is a little bit greater')
# else:
#     print('Wrong. The number is a little bit lesser')

# print('Ended')

# Оператора switch в python НЕТ!

# Оператор while - оператор цикла. Может иметь необязательный пункт else. Блок else не выполнится если цикл будет
# прерван оператором break

num = 23
running = True

# while running:
#     guess = int(input('Enter a number : '))
#     if guess == num:
#         print('Congrats! You are right!')
#         running = False
#     elif guess < num:
#         print('Wrong. The number is a little bit greater')
#     else:
#         print('Wrong. The number is a little bit lesser')
# else:
#     print('"while" cycle is ended up')

# Цикл for ..in перебирает коследовательность ключей объекта. Имеет опциональный блок else. Прерывание цикла оператором
# break приводит к пропуску блока else

# range - создает последовательность от первого аргумента до второго (не включительно). Третий аргумент указывает шаг.
# list(range(a, b, c)) - создаст список чисел от a до b с шагом c. Списки также можно перебирать циклом for

# for i in range(1, 5):
    # print(i)
# else:
    # print('The "for" cycle is ended up')

# оператор break. Прерывает цикл (while, for) досрочно. Блок else не выполняется

# len(String) - возвращает (число) длину строки

# while True:
#     s = input('Input some string: ')
#     if s == 'exit':
#         break
#     print('Length of the string is: ', len(s))
# print('Ending')

# оператор continue. Прерывает текущую итерацию цикла и переходит к следующей

while True:
    s = input('Input some string: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('Too short!')
        continue
    print('The length of the entered string is enough')
