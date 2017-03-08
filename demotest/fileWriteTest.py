# -*- coding:utf-8 -*-
import os


os.chdir("..")
print os.getcwd()
cwd=os.getcwd()

try:
    fo=open(cwd+"/logOutput/"+"testWrite.txt","w")
    for i in range(10):
        fo.write(str(i))
        fo.write("\n")
finally:
    print fo.encoding
    fo.close()


