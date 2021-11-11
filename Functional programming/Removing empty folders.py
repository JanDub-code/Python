import os

def rm_r("Users\RemoveKebab\OneDrive\Desktop\heh"):
    for i in os.listdir("Users\RemoveKebab\OneDrive\Desktop\heh"):
        p = os.path.join(path,i)
        
        if os.path.isdir(p):
            rm_r(p)
            os.rmdir(p)
            print('Removed dir:',p)
            
        else:
            os.remove(p)
            print('Removed file:',p)