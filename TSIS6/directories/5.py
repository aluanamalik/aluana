import os
lst = [1,2,3,4,5]
with open('main_dir/first/file2.txt', mode = "w") as file:
    file.write(str(lst) + "\n")
    file.close()
