import os
path = 'main_dir/first/file1.txt'
with open(path) as file:
    print(f"The count of lines in {path} is {len(file.readlines())}")
    file.close()
