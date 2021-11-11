import os
def rm_r(path):
    for i in os.listdir(path):
        p = os.path.join(path,i)
        
        if os.path.isdir(p):
            rm_r(p)
            os.rmdir(p)
            print('Removed dir:',p)
            
        else:
            os.remove(p)
            print('Removed file:',p)