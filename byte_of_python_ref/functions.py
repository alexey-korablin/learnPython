#!/usr/bin/env python

# def <nameFunction>(...[args]): - пример объявления  функции


def say_hello():
    print('Hello!')


# say_hello()

# параметры - имена, указанные в объявлении функции
# аргументы - значения с которыми вызывается функция

# переменная, объявленная внутри функции ограничена областью видимости этой функции. Снаружи функции она видна не будет
# объявление локальной переменной с тем же именем, что и у внешней переменной не повлияет на значение внешней переменой
# оно будет перезаписано внутри функции

x = 50


def func(x):
    print('x is ', x)
    x = 2
    print('x has been changed with ', x)


# func(x)
# print('x still is ', x)

# ключевое слово global позволяет сделать переменную глобальной
# использование ключевого слова global для объявления лоакльной переменной с тем же именем. что и у внешней приведет к
# перезаписи значения внешней переменной. Такое использование global не приветствуется. Объявления с global должны быть
# в самом внешнем блоке.
# Возвможно объявление сразу нескольких глобальных переменных global a, b, c, d

x = 50


def func():
    global x
    print('x is ', x)
    x = 2
    print('change the global x with ', x)


# func()
# print('x is ', x)

# nonlocal - указывает, что переменная не является локальной. Используется во вложенных функциях


def func_outer():
    x = 2
    print('x is ', x)


    def inner_func():
        nonlocal x
        x = 5


    inner_func()
    print('the local x has been changed with ', x)


# func_outer()

# необязательные параметры функции могут иметь значения по умолчанию и будут присвоены при вызове функции без
# соответствующих аргументов. def f(a=1): - a=1 -> параметр "а" получит значение "1" в случае если функция f будет
# вызвана без аргументов
# !!! значения по умолчанию могут находиться только в конце списка параметров. def f(a=2, b) - недопустимый синтаксис


def say(message, times=1):
    print(message * times)


# say('Hello')
# say('hello', 5)

# Ключевые параметры позволяют задавать значение аргументов обращаясь к их именам не следя за порядком перечисления
# параметров в объявлении функции. Объявлеине: def f(a, b=1, c=2): Вызов: f(c=7, a=5) Результат: a == 5, b == 1, c == 7


def func(a, b=5, c=10):
    print('a is', a, ', b is', b, ', c is', c)


# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

# переменное число параметров можно указать с помощью символа "*". "*" - означает позиционные параметры (собираются в
# кортеж). "**" - означает ключевые параметры (собирается в словарь)


def total(initial=5, *nums, **kwrds):
    print('initial is', initial, 'nums is', nums, 'kwrds is', kwrds)
    count = initial
    for num in nums:
        count += num
    for key in kwrds:
        count += kwrds[key]
    return count


# print(total(10, 1, 2, 3, vegetables=50, fruits=100))

# если параметр должен быть доступен только по ключу, то его следует указать в списке параметров сразу после параметра
# со "звездочкой". def f(a, b=2, *c, d) - теперь параметр d не может быть позиционным
# если нужны только ключевые параметры, но не нужны параметры со "звездочкой", то можно указать "*" без имени.
# def(a=1, *, b=2)


def total(init=5, *nums, extra_num):
    count = init
    for num in nums:
        count += num
    count += extra_num
    print(count)


# total(10, 1, 2, 3, extra_num=50)
# total(10, 1, 2) # упадет с ошибкой, так как параметр extra_num не имеет дефолтного значения и не указан в аргументах

# return используется для возврата значения из функции с последующим (досрочным) выходом из нее
# return без указания возвращаемого значения иквивалентен return None . None - тип данных, означает "ничего"
# вконце каждой функции неявно используется return None. См пример с some_func
# оператор pass используется для пустого блока команд

def max(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        print('The numbers are equal')


# print(max(2, 3))


def some_func():
    pass


# docstrings - строки документации доступные через "'''...'''". Позволяют писать пояснения к функции и получать их через
# обращение к методу __doc__ . Также получить строку документации можено вызвав функцию help(f), где f - функция, класс
# или модуль по которому нужно получить справку


def print_max(a, b):
    '''Returns the biggest from two corresponded numbers.

Both of passed numbers should be integers'''
    a = int(a)
    b = int(b)

    if a > b:
        print(a, 'is the biggest number')
    else:
        print(b, 'is the biggest number')


help(print_max)
print_max(12, 46)
print(print_max.__doc__)