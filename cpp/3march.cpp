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
/*
task  : 1  first  plz generate the pin  deposit  withdraw ==> ask user to enter the  pin and verify it . 
*/