import os, shutil

root = os.getcwd()
for dirpath, dirnames, filenames in os.walk(root):
    if '.svn' in dirnames:
        absPath = os.path.join(dirpath, '.svn')
        shutil.rmtree(absPath)
