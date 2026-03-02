# file  : txt  
"""
mode  : 

1. read mode  : file read only  ==> exiting file  read 
2. write  mode  :  new file create , write  ==>  exiting file  open ==> overwrite  
3. append  mode  :  new file create , write  ==>  exiting file  open ==> append

with open  :  file open 
close  file  close  
f.write () 
f.read()
"""
# w : 
"""
with  open("vyom.txt","w") as file : 
        file.write("hello world.\n")
        file.write("my name is vyom.\n")
        file.write("study in LJ.\n")
        file.write("favourite player is  virat kohli.\n")
        file.close()

"""
"""
with  open("vyom.txt","w") as file : 
        file.write("dashing handsome boy.\n")
        file.write("dream is to meet lionel messi.\n")
        file.close()
"""

#a : 
"""
with  open("vyom.txt","a") as file : 
        file.write("live on ahmedabad.\n")
        file.write("food lover.\n")
        file.close()
"""
"""with  open("vyom1.txt","a") as file : 
        file.write("live on ahmedabad.\n")
        file.write("food lover.\n")
        file.write("favourite professor is  rahul sir.  ")
        file.close()
"""

# r : 

"""
with open("vyom.txt","r") as file :
    # context = file.read()  # read whole file 
    # context = file .readline()  # read only  one  line .
    context = file.readlines()
    print(context)
"""
