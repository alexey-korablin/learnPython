#!/usr/bin/env python

import os
import time
import zipfile

# Для выполненеия этой задачи в OS Windows нужно установить программу GnuWin32

source = ['D:\\loki\\legacy\\python3\\learnPython\\byte_of_python_ref\\data',
          'D:\\loki\\legacy\\python3\\py3-simple_2d_game']
target_dir = 'D:\\loki\\legacy\\python3\\learnPython\\byte_of_python_ref\\backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter your comment ---> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

print('Folder has been created successfully', today)

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
print(zip_command)

# os.system(<command>) -> исполняет системную команду и возвращает код ее завершения. 0 - успех
# if os.system(zip_command) == 0:
#     print('backup created successfully', target)
# else:
#     print('Backup creating was failed')

for root, dirs, files in os.walk(source[1]):
    print(root)
    print(dirs)
    print(files)

