# file  handling  : 
"""
file  ==> read write append  ==> file  ==>  txt file   

1. read : r ==>  file read  ==> new file not created 
2. write : w ==>  file write  ==> new file created  ==> write  ==> exiting  ==> overwrite 
3. append : a ==>  file append  ==> new file created  ==> write  ==> exiting  ==> not overwrite


function  : 

with  open  ==> file  open  
close ==> file  close 
seek ==> cursor position  move 
write  ==> file  write

"""

# write  mode  : 

"""
with  open("arpit_jain.txt","w") as file:
    file.write("hello arpit.\n")
    file.write("how are you ???.\n")
    file.write("do you have any GF ????.\n") 
    file.write("yeassss sir .\n")
    file.close()
    
"""

# write  mode  exiting  file  : 
"""
with  open("arpit_jain.txt","w") as file:
    file.write("my name arpit.\n")
    file.write("live in ahmedabad.\n")
    file.write("study  in LJ ????.\n") 
    file.write("love to play cricket.\n")
    file.close()
"""

# append mode : 
"""with  open("arpit_jain.txt","a") as file:
    file.write("how are you ???.\n")
    file.write("do you have any GF ????.\n") 
    file.write("yeassss sir .\n")
    file.close()
"""
"""
with  open("arpit_jain2.txt","a") as file:
    file.write("how are you ???.\n")
    file.write("do you have any GF ????.\n") 
    file.write("yeassss sir .\n")
    file.close()
"""

# read mode : 
with  open("vyom.txt","r") as file :
    # content = file.read()
    # content =file.readline()
    content =file.readlines()
    
    print(content)