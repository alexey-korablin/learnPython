#!/usr/bin/env python

import os
import time

# Для выполненеия этой задачи в OS Windows нужно установить программу GnuWin32

source = ['D:\\loki\\legacy\\python3\\learnPython\\byte_of_python_ref\\data',
          'D:\\loki\\legacy\\python3\\py3-simple_2d_game']
target_dir = 'D:\\loki\\legacy\\python3\\learnPython\\byte_of_python_ref\\backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

# os.system(<command>) -> исполняет системную команду и возвращает код ее завершения. 0 - успех
if os.system(zip_command) == 0:
    print('backup created successfully', target)
else:
    print('Backup creating was failed')