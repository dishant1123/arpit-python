/*
protected : within the class and its derived classes

*/

// ex :1 
/*
#include <iostream>
using namespace std;
class student 
{
    protected : 
        int rollno =1; 
        string name="vyom";
    
};
class teacher : public student
{
    public :    
    void  show()
    {
        cout<<"rollno is : "<<rollno<<endl;
        cout<<"name is : "<<name<<endl;
    }
};

int main()
{
    teacher t1; 
    // cout<<"rollno is  : "<<s1.rollno;
    // cout<<"name is : "<<s1.name<<endl;
    t1.show();
    return 0;
}
*/
/*
#include <iostream>
using namespace std;
class bank
{
    public : 
        string ac_holder_name ="vyom";
        string bank_name = "Axis"; 
        string branch ="navranpura"; 
        int  balance =25000;
    
    void deposit(int amt)
    {
        balance += amt;
        cout<<"deposit amt is  : "<<amt<<endl;
    }
    void withdraw(int amt) // 35000 
    {
        if(balance -amt >=10000) // 35000 -3000 >=10000 
        {
            balance -= amt;
            cout<<"withdraw amt is  : "<<amt<<endl;
        }
        else 
        {
            cout<<"min balance  required is 10000 rs"<<endl;
        }
    } 
    void check_balance()
    {
        cout<<"balance is : "<<balance<<endl;
    }
    void show()
    {
        cout<<"ac holder name is : "<<ac_holder_name<<endl;
        cout<<"bank name is : "<<bank_name<<endl;
        cout<<"branch is : "<<branch<<endl;
        cout<<"initial balance is : "<<balance<<endl;
    }
};

int main()
{
    bank b1; 
    b1.show(); 
    b1.deposit(10000); 
    b1.withdraw(18000); 
    b1.check_balance();
    return 0;
}
*/
/*
task  : 1  first  plz generate the pin  deposit  withdraw ==> ask user to enter the  pin and verify it . 

*/

// constructor   : automatically called when an object is created.
/*
rule  :
1. class name = constructor name 
2. no return type  

types : 
1. default constructor
2. parameterized constructor
3. non-parameterized constructor
4. copy constructor
5. constructor overload 
*/
// ex :1 
/*
#include <iostream>
using namespace std;
class student 
{
    public :
        student()
        {
            cout<<"default constructor called"<<endl;
        }
};
int main()
{
    student s1; 
    return 0;
}
*/ 

// ex :2 non-parameterized constructor
/*
#include<iostream>
using namespace std;
class student 
{
    public : 
        int  rollno; 
        string name; 
    student()
    {
        rollno =1; 
        name ="vyom";
    }
    void  show()
    {
        cout<<"rollno is : "<<rollno<<endl;
        cout<<"name is : "<<name<<endl;
    }
};
int main()
{
    student s1; 
    s1.show(); 
    return 0; 
}
*/
// ex :3 parameterized constructor
/*
#include<iostream>
using namespace std;
class student 
{
    public : 
        int  rollno; 
        string name; 
    student(int  r , string  n)
    {
        rollno =r; 
        name =n;
    }
    void  show()
    {
        cout<<"rollno is : "<<rollno<<endl;
        cout<<"name is : "<<name<<endl;
    }
};
int main()
{
    student s1(1,"vyom");
    student s2(2,"arpit");
    s1.show(); 
    s2.show();
    return 0; 
}
*/
// ex :4 copy constructor
/*
#include<iostream>
using namespace std;
class student
{
    public :
        int  rollno;
        string name;
    student(int  rollno, string  name)
    {
        this->name =name; 
        this->rollno =rollno;
    }
    student(const student &s)
    {
        rollno =s.rollno; 
        name =s.name;
    }
    void show()
    {
        cout<<"rollno is : "<<rollno<<endl;
        cout<<"name is : "<<name<<endl;
    }
};
int main()
{
    student s1(1,"vyom");
    
    student s2(s1);
    s2.show(); 
    return 0; 
}
*/ 

// ex :5 constructor overload

#include<iostream>
using namespace std;
class student 
{
    public : 
        int  rollno; 
        string name;
    student()
    {
        cout<<"default constructor called"<<endl;
    }
    student(string name)
    {
        rollno =1; 
        this->name =name;
        cout<<"non parameterized constructor called"<<endl;
    }
    student(int  rollno, string  name)
    {
        this->rollno =rollno;
        this->name =name;
        cout<<"parameterized constructor called"<<endl;
    }
    void show()
    {
        cout<<"rollno is : "<<rollno<<endl;
        cout<<"name is : "<<name<<endl;
    }
};
int main()
{
    student s1; 
    student s2("arpit");
    s2.show();
    student s3(1,"vyom");
    s3.show();
    return 0; 
}