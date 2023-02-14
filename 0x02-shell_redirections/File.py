import os
fileName = input("The file name :")
os.system("echo \"#!/bin/bash \" >"+ fileName)
os.system("chmod u+x "+ fileName)
cmd = input("commands : ")

os.system(cmd +">>"+fileName)
