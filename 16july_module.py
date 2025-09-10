# module  : math  c-math  random date time  datetime calender time delta   
 
import random as r 

# print(r.random())  # 0-1  float value  
# print(r.randrange(1,10,2))  # last value  excluded 
# print(r.randint(1,5))  # 1, 5 both are included 

# print(r.choice([1,2,3,4,"vyom","arpit"]))

# print(r.choices([1,2,3,4,"vyom","arpit"],k=3))

"""
l1 =[1,2,3,4,"vyom","arpit"]
print(l1)

r.shuffle(l1)
print(l1)
"""

"""
rock paper scissor : 
"""

"""def main():
    user_score =0
    computer_score =0

    for i in range(5):

        print("welcome to rock paper scissor")
        print("enter your choice : rock/paper/scissor")
        user_choice = input("enter  your choice : ")
        computer_choice = r.choice(["rock","paper","scissor"])

        if user_choice =="rock" and computer_choice =="rock" or user_choice =="paper" and computer_choice =="paper" or user_choice =="scissor" and computer_choice =="scissor":
            print("tie")
        
        elif user_choice =="rock" and computer_choice =="scissor" or user_choice =="paper" and computer_choice =="rock" or user_choice =="scissor" and computer_choice =="paper":
            print("user wins")
            user_score +=1
        else :
            print("computer wins")
            computer_score +=1

    print(f"user score : {user_score}  computer score : {computer_score}")
    if user_score > computer_score :
        print("user win match ")
    else :
        print("computer win match")
main()
"""
# 
"""
task  2 : computer  guess one  number  nad you have  it guess in 5 attempts .

computer_guess= r.randrange(1,20)  #13 

attempts =5 
11
6
7
13
print(f"computer guess : {computer_guess}")
"""

# from package import arpit as a 

# a.h()

"""from package import vyom as v 

print(v.add(10,12))
"""