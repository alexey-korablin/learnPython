#!/usr/bin/env python

# try - содержит логику, в которой может возникнуть исключение.
# except <name-of-the-exception> - содержит логику обработки исключения. Если после except указано имя, то такой блок
# будет перехватывать только соответствующие исключения, иначе перехватит все исключения.
# Блок else срабатывает если в блоке try не возникло исключений

# try:
#     text = input('Enter something --> ')
# except EOFError:
#     print('Why you make me EOF?')
# except KeyboardInterrupt:
#     print('You have interrupted the operation.')
# else:
#     print('You have entered {0}'.format(text))


# Вызов исключений

# raise - оператор, вызывающий исключение. Аргументы - имя ошибки и объект исключения. Вызываемая ошибка должна
# наследоваться от класса Exception


# class ShortInputException(Exception):
#     '''User's exception class'''
#     def __init__(self, length, at_least):
#         Exception.__init__(self)
#         self.length = length
#         self.at_least = at_least
#
#
# try:
#     text = input('Enter something --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
# except EOFError:
#     print('Why you make me EOF?')
# except ShortInputException as ex:
#     print('ShortInputException: The length of the entered string -- {0}; \
# expected at least {1}'.format(ex.length, ex.at_least))
# else:
#     print('The exception does not occur')


# Finally

# блок finally указывается после всех except-блоков и выполняется всегда

# import time
#
# try:
#     f = open('./data/poem.txt')
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         time.sleep(2)
# except KeyboardInterrupt:
#     print('You did interrupt the reading of the file!!!')
# finally:
#     f.close()
#     print('(Clearing: closing of the file)')


# With

# оператор with выполняет открытие, чтение и закрытие файла

with open('./data/poem.txt') as f:
    for line in f:
        print(line, end='')


