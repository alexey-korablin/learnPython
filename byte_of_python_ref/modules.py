#!/usr/bin/env python

# !!! импорт модулей отностиельно дорогостоящая операция. Для ускорения процесса модули следует хранить в файлах с
# расширением .pyc (данные файлы будут содержать байткод). Таким образом при импорте модуля Python уже не будет тратить
# ресурсы на интерпритацию кода

# При импорте модуля, содержащийся в нем код исполняется

# импорт модуля sys в программу для дальнейшего его использования
# в примере ниже используется свойство argv модуля sys. argv содержит список аргументов командной строки, которые
# хранятся в виде строк

# import sys
#
# print('Arguments of the command line:')
# for i in sys.argv:
#     print(i)
#
# print('The variable PYTHONPATH contains', sys.path, '\n')

# метод getcwd модуля os возвращает путь к текущему каталогу (current working directory)

# import os
#
# print(os.getcwd())

# ключевое слово from позволяет импортировать не весь модуль, а его отдельное свойство или метод

# from math import sqrt
#
# n = input('Enter a range: ')
# p = [2, 3]
# count = 2
# a = 5
# while count < int(n):
#     b = 0
#     for i in range(2, a):
#         if i <= sqrt(a):
#             if a % i == 0:
#                 print('a is complex', a)
#                 b = 1
#             else:
#                 pass
#     if b != 1:
#         print('a is simple', a)
#         p += [a]
#     count += 1
#     a += 2
#
# print(p)

# __name__ - свойство которое содержится в каждом модуле. Указывает на то как это модуль был запущен. Если как отдельная
# программа, то его значение будет равно __main__
# альтернативный вариант доступен из REPL: >>> import modules

# if __name__ == '__main__':
#     print('The program has been launched by itself')
# else:
#     print('The program is using another module')

# СОЗДАНИЕ МОДУЛЯ

# file_name - mymodule.py


# def sayhi():
#     print('Hi! The MYMODULE speaks!')
#
#
# __version__ = '0.1'
#
# # file_name - mymodule_demo.py
#
# import mymodule
#
# mymodule.sayhi()
# print('Version', mymodule.__version__)

# Или можно импортировать не модуль целиком а отдельные компоненты. Например
# file_name - mymodule_demo.py

# from mymodule import sayhi, __version__
#
# sayhi()
# print('Version is ', __version__)

# The Zen of Python
# import this

# dir() -> возвращает имена всех идентификаторов доступных в текущем модуле. dir(sys) -> вернет имена идентификаторов
# доступных в модуле sys

# import sys
#
# dir(sys)
# dir()
