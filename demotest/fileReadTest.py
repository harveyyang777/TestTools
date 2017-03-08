# -*- coding:utf-8 -*-

'''
try:
    fo=open("test.txt","r")
    fr=fo.readlines()
    for i in fr:
        print i.rstrip()
finally:
    fo.close()

'''

try:
    fo=open("test.txt","r")
    fr=fo.readline()
    print fr.rstrip()
    print fo.readline().rstrip()
    print fo.tell()
finally:
    fo.close()




