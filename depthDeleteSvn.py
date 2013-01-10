import os
import shutil
import stat

def on_rm_error( func, path, exc_info):
    os.chmod( path, stat.S_IWRITE )
    os.unlink( path )
iters = 0
def dig(path):
    pathRoot = path+"\\"
    for f in os.listdir(pathRoot):
         if f.endswith(".svn"):
             print("Efface ",pathRoot+f)
             iters+=1
             shutil.rmtree( pathRoot + f, onerror = on_rm_error )
         elif os.path.isdir(pathRoot + f):
             dig(pathRoot + f)
         
dig(os.getcwd())
print("Terminé. ",iters,"fichiers effacés.")
input("Entrez qqc pour quitter.")