"""
1. r+ : read==> cursor move  and    write ==> letter  over write   ==> exiting  file      
2. w+ : write and read 
3. a+ : append and read 
"""
# r + : 
"""with  open("vyom.txt","r+") as file :
    file.write("my name is jainam.\n")
    file.write("dream is study in AU.")
    file.seek(0)  # ==> cursor at the start of the file

    context =  file.read()
    print(context)
    file.close()
"""

# w + : 
"""with  open("arpit.txt","w+") as file : 
    file.write("my name is jainam.\n")
    file.write("dream is study in AU.\n")
    file.write("live in ahmedabad.\n")
    file.seek(0) 
    context =file .read()
    print(context)
    file.close()
"""
"""
with open("vyom1.txt","w+") as file :  # exiting  file  
    file.write("my name is kirtan.\n")
    file.write("dream to meet PM Narendra Modi.\n")
    file.seek(0)
    context =file .read()
    print(context)
    file.write("live in ahmedabad.\n")
    file.close()
"""

# a+ : 
"""with open("vyom1.txt","a+") as file :  # exiting  file  
    file.write("my name is arpit.\n")
    file.write("dream to meet President Donald Trump.\n")
    file.seek(0)
    context =file .read()
    print(context)
    file.close()
"""

# csv file read : 

