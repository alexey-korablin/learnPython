#!/usr/bin/env python

# СПИСКИ
# функция len(<list>) возвращает длинну массива
# shop_list = ['apples', 'mango', 'carrot', 'banana']
#
# print('I should do', len(shop_list), 'purchases')
#
# print('Purchases:', end=' ')
#
# for item in shop_list:
#     print(item, end=' ')
#
# print('\nAs well it needs to buy rice')
#
# # Метод .append(<appended_element>) позволяет добавить элемент в конец списка
# shop_list.append('rice')
#
# print('Now my purchase list is:', shop_list)
#
# print('Let\'s sort the list')
# # Метод .sort() сортирует список, изменяя его
# shop_list.sort()
#
# print('Now sorted list looks like that:', shop_list)
#
# print('The first purchase that I need to do is', shop_list[0])
#
# old_item = shop_list[0]
#
# # оператор del удаляет переданный ему элемент из списка -> del list_q[0]
# del shop_list[0]
#
# print('I bought', old_item)
#
# print('My shop list now looks like', shop_list)

# КОРТЕЖИ
# zoo = ('python', 'elephant', 'penguin')
#
# # Функция len(<tuple>) таде возвращает длину кортежа
# print('The number of animals in the zoo', len(zoo))
#
# new_zoo = 'monkey', 'camel', zoo
#
# print('Number of cages at the zoo -', len(new_zoo))
# print('Animals in the new zoo', new_zoo)
# print('The animals drove from the old zoo', new_zoo[2])
# print('The last animal that has been driven from the old zoo', new_zoo[2][2])
# print('Number of the animals in the new zoo', len(new_zoo) - 1 + len(new_zoo[2]))

# СЛОВАРИ
# !!! Ключи словаря должны быть уникальными.
# !!!Ключи могут быть только неизменяемыми объектами, такими как строки

# addresses = {
#     'Swaroop': 'swaroop@swaroopch.com',
#     'Larry': 'larry@wall.org',
#     'Matsumoto': 'matz@ruby-lang.org',
#     'Spammer': 'spammer@hotmail.com'
# }
#
# print('The Swaroop\'s address is', addresses['Swaroop'])
#
# del addresses['Spammer']
#
# print('\nThe address book contains {0} contacts'.format(len(addresses)))
#
# # Метод .items() у словарей возвращает пару ключа и значения, которые могут быть сохранены в переменные
# for name, address in addresses.items():
#     print('The contact {0} has address {1}'.format(name, address))
#
# addresses['Guido'] = 'guido@python.org'
#
# # Оператор in позволяет проверить вхождение ключа в словарь
# if 'Guido' in addresses:
#     print('\nGuido\'s address is', addresses['Guido'])

# ПОСЛЕДОВАТЕЛЬНОСТИ

shop_list = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Индексирование
# print('The element 0 -', shop_list[0])
# print('The element 1 -', shop_list[1])
# print('The element 2 -', shop_list[2])
# print('The element 3 -', shop_list[3])
# print('The element -1 -', shop_list[-1])
# print('The element -2 -', shop_list[-2])
# print('The zeroth symbol is', name[0])
#
# # Срез
# print('The elements from 1 to 3', shop_list[1:3])
# print('The elements from 2 up to end', shop_list[2:])
# print('The elements from 1 to -1', shop_list[1:-1])
# print('The elements from start to end', shop_list[:])
# print('The symbols from 1 to 3', name[1:3])
# print('The symbols from 2 up to end', name[2:])
# print('The symbols from 1 to -1', name[1:-1])
# print('The symbols from the start to the end', name[:])

# Шаг среза задается третим аргументом. Он может быть отрицательным. В этом случае элементы будут возвращены в обратном
# порядке
# print(shop_list[::1])
# print(shop_list[::2])
# print(shop_list[::3])
# print(shop_list[::-1])

# МНОЖЕСТВА
# Является неупорядоченным набором объектов. Одинаковые объекты во множестве могут встречаться неоднократно
# bri = set(['Brazil', 'Russia', 'India'])
# print('India' in bri)
# print('USA' in bri)
#
# bric = bri.copy()
# bric.add('China')
#
# print(bric.issuperset(bri))
#
# bri.remove('Russia')
# # Оператор & во множествах показывает имеющиеся пересечения. Возможно сначала нужно проверить являются ли они под- или
# # надмножествами друг друга. set_a.issubset(set_b) или set_a.issuperset(set_b) => set_a & set_b
# # set_a.intersection(set_b) вернет тот же результат, что и set_a & set_b
# print(bri & bric)
# print(bri.intersection(bric))

# ССЫЛКИ

# shop_list = ['apple', 'mango', 'carrot', 'banana']
# # передача по ссылке
# my_list = shop_list
#
# del shop_list[0]
#
# # общий объект изменен
# print('shoplist:', shop_list)
# print('mylist', my_list)
#
# # Копирование элементов в новый объект
# new_list = shop_list[:]
# del new_list[0]
#
# # теперь это два разных объекта
# print('shoplist:', shop_list)
# print('newlist', new_list)

# Некоторые методы строк
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, this string starts with "Swa"')

if 'a' in name:
    print('Yes, the string contains letter "a"')

if name.find('war') != -1:
    print('Yes, the string contains string "war"')

delimiter = '_*_'
my_list = ['Brazil', 'Russia', 'India', 'China']

print(delimiter.join(my_list))

