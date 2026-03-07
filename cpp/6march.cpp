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

// ex :3 multi level inheritance
/*
class a 
class b : public a 
class c: public b
*/

#include <iostream>
using namespace std;
class employees 
{
    private : 
        string  name; 
    protected : 
        int  age; 
    public : 
        employees(string n, int a)
        {
            name =n; 
            age =a; 
        }
    void show()
    {
        cout<<"name : "<<name<<"\n";
    }
};
class manager : public employees 
{
    public : 
        string department; 
    manager(string n, int a, string d):employees(n,a) // called base class constructor
    {
        department = d;
    }
};
class senior_manager : public manager
{
    private : 
        int salary; 
    public : 
        senior_manager(string n , int a, string d, int s):manager(n,a,d)
        {
            salary = s;
        }
    void display()
    {
        show(); 
        cout<<"age is  : "<<age<<"\n";
        cout<<"department is : "<<department<<"\n";
        cout<<"salary is : "<<salary<<"\n";
    }
};
int main()
{
    senior_manager s("arpit",23,"computer",10000); 
    s.display(); 

    manager m("vyom",19,"R & D");
    m.show();
    cout<<"department : "<<m.department<<"\n";
    return 0;
}