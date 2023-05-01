import os

path = 'main_dir/first/file2.txt'

if os.path.exists(path):
    print('File exists')
else:
    print('File does not exist')

if os.access(path, os.R_OK):
    print('File is readable')
else:
    print('File is not readable')


if os.access(path, os.W_OK):
    print('File is writable')
else:
    print('File is not writable')


if os.path.isfile(path) and (path.endswith('.exe') or path.endswith('.bat') or path.endswith('.cmd')):
    print('File is executable')
else:
    print('File is not executable')
