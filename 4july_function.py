# function  : 
"""
1. no arg  no return 
2 . with arg  no return
3. no arg  with return
4. with arg  with return
"""

# no arg no return
"""
def sum():
    a =10 
    b =20 
    c=a+b
    print("sum of a and b is ",c)

sum()
"""
# with arg no return
"""
def sum(a,b):
    c=a+b
    print("sum of a and b is ",c)
a= int(input("enter a number"))
b= int(input("enter a number"))
sum(a,b)
"""
# no arg with return
"""
def sum():
    a=10
    b=45
    c=a+b
    return c 
print(sum())
"""

# with arg with return
"""
def sum(a,b):
    c=a+b
    return c 
a = int(input("enter a number: "))
b = int(input("enter a number: "))
print(sum(a,b))
"""
# *arg   :takes  only numreic  arg  : 

"""
def sum1(*arg):
    a= sum(arg)
    return a
print(sum1(12,45,6,7,8,99,11,22,33,44,89.90))
"""

# **kargs : use dict , key  value 

"""def d1(**kargs):
    for  i , j in  kargs.items():
        print(i, ":", j)
d1(name="yash",gf="pata nia",age=20,city="ahm")
"""

# local variable  :  with in function accessible 

"""def local():
    x =10   # local variable  
    print("local variable x is ", x)
local()
# print(x)  not accessible  outside function 

"""

# global variable  : accessible  outside function , in-side function

"""
x =100 
def yash():
    print("global variable x is inside function ", x)
yash()
print("global variable x is outside function ", x)  # accessible outside function
"""

"""
bank  application  : 
1. create account  : user name  password  : 
2. login :  user name  password  match    login success
only sucessfull  ==> 25000  
3. deposit  : amount  :  add to balance
4. withdraw : amount  :  deduct from balance
5. check balance : display current balance 

"""
def login(user, password):
    user1 = input("Enter user name: ")
    password1 = input("Enter password: ")
    if user == user1 and password == password1:
        print("Login success")
        return True
    else:
        print("Login failed")
        return False
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit success")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdraw success")
    return balance

def check_balance(balance):
    print("Current balance is:", balance)
    return balance

def main():
    user = ""
    password = ""
    logged_in = False
    balance = 0

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check balance")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            user = input("Enter new user name: ")
            password = input("Enter new password: ")
            print("Account created successfully!")

        elif choice == 2:
            if login(user, password):
                logged_in = True
                balance = 25000
            else:
                logged_in = False

        elif choice == 3:
            if logged_in:
                balance = deposit(balance)
            else:
                print("Please login first.")

        elif choice == 4:
            if logged_in:
                balance = withdraw(balance)
            else:
                print("Please login first.")

        elif choice == 5:
            if logged_in:
                check_balance(balance)
            else:
                print("Please login first.")

        elif choice == 6:
            print("Thank you for using the bank app.")
            break

        else:
            print("Invalid choice.")

main()
