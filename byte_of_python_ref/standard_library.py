#!/usr/bin/env python

# МОДУЛЬ SYS

# Модуль sys содержит функциональность, характерную для системы.
# Просмотр версии интерпритатора .version_info

# import sys
#
# print(sys.version_info)
# print(sys.version_info[0] >= 3)

# Модуль warnings служит для отображения предупреждения пользователю.
# Принимаемые аргументы: .warn(message, category, stacklevel source)

# import sys
# import warnings
#
# if sys.version_info[0] >= 3:
#     warnings.warn('To execute this program needs Python v2.x', RuntimeWarning)
# else:
#     print('Normal continue')


# МОДУЛЬ LOGGING

# Модуль logging позволяет осуществлять логирование работы программ

import os
import platform
import logging

PATH = 'D:\Alexey\dev\learn\python\\bop\learnPython\\byte_of_python_ref\data'

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(PATH, 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Saves the log into:', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)

logging.debug('The beginning of the program')
logging.info('Some actions')
logging.warning('The program dies')
