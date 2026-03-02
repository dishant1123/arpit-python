"""
* * * * *  *           * * * * * 
* * * * *  * *         * * * *
* * * * *  * * *       * * * 
* * * * *  * * * *     * *
* * * * *  * * * * *   *
"""

"""for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
#2 :    
"""
for i in range(1,6):  # 2  
    for j in range(1,i+1): # 1,3  
        print("*",end=" ")  #  * 
    print()                  # * *
"""

#3 :
"""
for i in range(6,1,-1):  # 2  
    for j in range(1,i): # 1,3  
        print("*",end=" ")  #  * 
    print()                  # * *
    
"""

"""
1
12
123
1234
12345
"""
"""
for i in range(1,6):  #2 ,6
    for j in range(1,i+1): # 2,3   
        print(i,end=" ")  # 1   
    print()               # 2 2 
"""

"""
a 
a b 
a b c
a b c d
a b c d e
"""
"""
for i in range(1,6):  # 2 ,6  
    ch=97
    for j in range(i): #  0 1  
        print(chr((ch+j)),end=" ")  #   a  
    print()                  #          a b 
"""

"""
5.          6.               7.          8.       
* * * * *    * * * * *        *         *
  * * * *     * * * *       * *        * * 
    * * *      * * *      * * *       * * *
      * *       * *     * * * *      * * * * 
        *        *    * * * * *     * * * * * 
"""

# 5 : 
"""
for i in range(1,6):  # 2  
    for k in range(1,i):  # 1,2 
        print(" ",end=" ")  
    for j in range(5,i-1,-1): # 5 1   
        print("*",end=" ")    # * * * * *   
    print()                   #   * * * *
"""

# 6 :
"""
for i in range(1,6):  # 2  
    for k in range(1,i):  # 1,2 
        print(" ",end="")  
    for j in range(5,i-1,-1): # 5 1   
        print("*",end=" ")    # * * * * *   
    print()                   #   * * * *
"""

# 7 :
"""for i in range(1,6):  #  
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1): # 1,3  
        print("*",end=" ")  #  * 
    print()                  # * *
""" 

# 8 :
"""for i in range(1,6):  #  
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1): # 1,3  
        print("*",end=" ")  #  * 
    print()                  # * *
"""

# 9 :
"""for i in range(1,5):  #  
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1): # 1,3  
        print("*",end=" ")  #  * 
    print()                  # * *
for i in range(1,6):  # 2  
    for k in range(1,i):  # 1,2 
        print(" ",end="")  
    for j in range(5,i-1,-1): # 5 1   
        print("*",end=" ")    # * * * * *   
    print()                   #   * * * *

"""

"""for i in range(1,5):  # 2  
    for j in range(1,i+1):
        if i % 2==0:  
            print("#",end=" ")
        else :
            print("*",end=" ")   
    print()                  
"""
"""
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""
# 10 :
"""
for i in range(1,5):  # 2  
    for j in range(1,i+1):
        if i % 2==0:  
            print("#",end=" ")
        else :
            print("*",end=" ")   
    print()
* * *
* * 
* 
"""

"""for i in range(1,5):
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for  j in range(5,i-1,-1):
        print("*",end=" ")
    print()
for i in range(1,5):
    for  k in range(5,i,-1):
        print(" ",end=" ")
    for  j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(1,6):
    for  k in range(1,i):
        print(" ",end=" ")
    for  j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     for space in range(1, (6 - i) * 2):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     for space in range(1, (6 - i) * 2):
#         print(" ", end=" ")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# Total number of rows
"""rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    # Middle spaces
    spaces = 2 * (rows - i)
    for s in range(spaces):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line

# Bottom half
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    spaces = 2 * (rows - i)
    for s in range(spaces):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line"""
# rev number  : 

"""
123 : 321 

456   : 654 
1234 : 4231 
"""

# n =int(input("Enter the number : "))

# convert = str(n)

# r =convert[-1] + convert[:-1]

# rev =int(r)
# print(rev)

