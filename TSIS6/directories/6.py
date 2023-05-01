import os

path = "main_dir/26files/"
for i in range(26):
    file = open(path + f"{chr(i+65)}.txt", "w+")
    file.close()
