import time 
import os 
import shutil

def removeFiles():
    path=input("enter path name for your folder")
    days = 30
    seconds=time.time()-(days*24*60*60)
    if(os.path.exists(path)):
        for root,dirs,files in os.walk(path):
            if(seconds>os.stact(path).st_ctime):
                shutil.rmtree(path)

removeFiles()
