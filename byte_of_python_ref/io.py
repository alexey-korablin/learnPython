#!/usr/bin/env python

# Ввод от пользователя

# palindromes = ['Don\'t nod.', 'I did, did I?', 'My gym', 'Red rum, sir, is murder', 'Step on no pets', 'Top spot',
#                'Was it a cat I saw?', 'Eva, can I see bees in a cave?', 'No lemon, no melon']
#
#
# def reverse(text):
#     return clean_text(text[::-1])
#
#
# def clean_text(text):
#     result = ''
#     symbol_list = [' ', ',', '.', '!', '?', '\'']
#     for letter in text:
#         if letter not in symbol_list:
#             result += letter
#     return result.lower()
#
#
# def is_palindrome(text):
#     return clean_text(text) == reverse(text)
#
#
# smth = input('Enter a text: ')
#
# if is_palindrome(smth):
#     print('Yes, it is a palindrome')
# else:
#     print('No, it is not a palindrome')

# Файлы.

# открывать и использовать файлы можно с помощью объекта класса file
# .read и .readline - методы для чтения из файла, .write - метод для записи в файл.
# При открытии файла нужно указать режим, дающий возможность читать или записывать данные. По умолчанию используется
# r -чтение
# .close - метод для закрытия файла.
# Режимы: r - чтение, w - запись, a - добавление
# Вид в котором открывается файл: t - текстовый, b - бинарный

# poem = '''\
# Программировать весело,
# Если работа скучна,
# Чтобы придать ей веселый тон -
#     используй Python!
# '''
#
# f = open('data/poem.txt', 'w')
# f.write(poem)
# f.close()
#
# f = open('data/poem.txt', 'r')
#
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line, end='')
#
# f.close()


# Pickle

# Для длительного хранения объект можно использовать встроеный модуль pickle

import pickle

shop_list_file = 'shoplist.data'
shop_list = ['apples', 'mango', 'carrot']

f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()

del shop_list

f = open(shop_list_file, 'rb')

stored_list = pickle.load(f)
print(stored_list)
