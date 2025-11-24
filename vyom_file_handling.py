# file  handling  :  txt file 
"""
1. read : exiting  file  open  ==> no new file create in read mode 
2. write : new file create  + write   ==> exiting file open ==> overwrite  
3. append :new file create  + write   ==> exiting file open ==> last add 

with open ("file name.txt","mode") as f  

f.close()
f.open()
f.read() ==> context read 
"""

# w :

"""
with  open("vyom_24nov.txt","w") as f :
    f.write("my name is  vyom gandhi.\n")
    f.write("my age is 20.\n")
    f.write("my hobby is cricket.\n")
    f.close()
"""
# w mode exiting file  open  : 

"""
with  open("vyom_24nov.txt","w") as f :
    f.write("dream to meet virat kohli\n")
    f.write("big  businessman. \n")
    f.write("huge property.\n")
    f.close()

"""

# read mode : 

"""
with open("vyom.txt","r") as f : 
    # context = f.read()  # all context  read from  file 
    # context = f.readline()  # first  line context  read from  file
    context =f.readlines()
    print(context)
"""

# append : 
with  open("vyom_24nov.txt","a") as f :
    f.write("best friend name  is  rishi.\n")
    f.write("dream to open 1 gym in ahm. \n")
    f.write("clg name is  LJ.\n")
    f.close()

