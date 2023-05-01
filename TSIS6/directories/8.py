import os
path = 'main_dir/second/file3.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print('File does not exist')
