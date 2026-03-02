"""
r+ , a+ , w+ : 

"""

# write , writelines :

"""with  open("vyom_24nov.txt","w") as f :
    f.write("my best friend name is yash parikh.\n")
    f.write("we will starting SQL with madhusudan sir very soon.\n")
    
    f.writelines(["bcz of dishant sir no authority to take sql.\n"])
    f.writelines(["now  we fighting with dhiraj sir and  starting sql with me."])
    f.close()
"""

# read + :  read + write  exiting file. 

"""
with  open("vyom.txt","r+") as f : 
    f.write("vyom p gandhi ")
    f.seek(0,2)
    context =f.read()
    print(context)
    f.close()
# vyom p gandhi nam.
# my name is jainam.   vyom p gandhi 
"""

# w +   :exiting file  open ==> overwrite 

"""
with  open("vyom.txt","w+") as f : 
    f.write("vyom p gandhi \n")
    f.write("my best friend name is yash parikh.\n")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()
"""

# a+ : exiting file  open ==> last add
"""
with  open("vyom16aug.txt","a+") as f : 
    # f.write("vyom p gandhi \n")
    # f.write("my best friend name is yash parikh.\n")
    # f.write("father name is parthiv bhai.\n")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()

"""
# a+ : exiting file  open ==> last add
"""with  open("vyom.txt","a+") as f : 
    # f.write("vyom parthiv gandhi \n")
    # f.write("my best friend name is rishi shah.\n")
    # f.write("father name is parthiv bhai.\n")
    f.seek(0)
    context =f.read()
    print(context)
    f.close()

"""

