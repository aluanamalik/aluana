import os
path = "main_dir/first"

with open(path + "/file1.txt", mode = 'r') as file1:
    lines1 = file1.readlines()

    file1.close()
with open(path + "/file2.txt", mode = 'w') as file2:
    for i in range(len(lines1)):
        file2.writelines(lines1[i])
    file2.close()
