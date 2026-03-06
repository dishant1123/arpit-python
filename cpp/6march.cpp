/*
inheritance : 

1.single inheritance
2.multiple inheritance
3.multi level inheritance
4. hirarchical inheritance
5. hybrid inheritance
*/

// ex :1 single inheritance
/*
#include <iostream>
using namespace std;
class student 
{
    public : 
        string  name; 
        int age; 
    // student(int a, string n)
    // {
    //     name =n; 
    //     age =a; 
    // }
    student()
    {
        name = "arpit";
        age = 21;
    }
};
class teacher : public student 
{
    public : 
        string subject; 
    
    teacher(string s):student() // base class constructor calling
    {
        subject = s;
    }
    void show()
    {
        cout<<"name : "<<name<<"\n";
        cout<<"age : "<<age<<"\n";
        cout<<"subject : "<<subject<<"\n";
    }
};
int main()
{
    teacher t("c++");
    t.show();
    return 0; 
}
*/ 

// ex :2 multiple inheritance
/*
class a 
class b 
class c : public a, public b
*/