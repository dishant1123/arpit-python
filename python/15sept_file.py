# file handling  : txt file   
"""
1. read  : r ==>  only  exiting file   , read  ==> data 
2. write  : w==> new file create  ==> write  ==>  exiting file  ==> overwrite 
3. append : a==> new file create  ==> write  ==>  exiting file  ==> append 

function  : 

fopen , with  open ==> file open  
fclose ==>  file  close 
fread ==> file read 
fwrite ==> file write 

"""
"""
with open("yash.txt","w") as file : 
    file .write("my name is yash parikh.\n")
    file .write("live in ahmedabad.\n")
    file .write("study in GLS.\n")
    file.close()
"""
# exiting file  ==> write  ==> overwrite 

"""with  open("yash.txt","w") as file :
    file .write("best friend name is ayaan shah.\n")
    file.write("dream to study  in AU.")
    file .close()
"""

# read : ==>  file  exiting  open  only 

"""with  open("vyom.txt","r") as file : 
    # context = file.read()  # read all data . 
    # context = file.readline()  # single  line read only  
    context = file.readlines()  # read all  lines  give in list . 
    print(context)
"""

#task :1 
"""
ask user to enter the  string  and  separate  print the vowel and consonant. 
input  : my name  is yash  parikh. 

vowel.txt :ae i a ai 
consonant.txt :my nm s ysh prkh.

"""