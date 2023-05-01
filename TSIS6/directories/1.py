import os

path = str("main_dir")
os.chdir(path)

# returns the catalog of directories
for i in os.listdir():
    print(f"{i} : {os.listdir(i)}")
