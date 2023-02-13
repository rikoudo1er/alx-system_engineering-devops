import os
os.system("git add * ")
commit = input(" commit message : ")
os.system("git commit -m \" Add file "+ commit +"\" ")
os.system("git push")
