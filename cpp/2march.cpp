/*
class object : 

access specifier :
1.public : accessible from anywhere
2.private : accessible only from the class
3.protected : accessible only from the class and its derived classes

*/

// ex :1
/*
#include <iostream>
using namespace std;
class student 
{
    public :
        // int  rollno =1; 
        // string name="vyom";
        int rollno; 
        string name;  
    void input()
    {
        cout<<"enter rollno : ";
        cin>>rollno; 
        cout<<"enter name : ";
        cin>>name; 
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
    // cout<<"rollno is  : "<<s1.rollno;
    // cout<<"name is : "<<s1.name<<endl;
    s1.input();
    s1.show();
    s1.name ="yash"; 
    s1.rollno =100;

    s1.show(); 
    return 0; 
}
*/

// ex :2 
#include <iostream>
using namespace std;
class student 
{
    private :
        int  rolllno=1 ;
        string name="vyom";
    public : 
        void show()
        {
            cout<<"rollno is : "<<rolllno<<endl;
            cout<<"name is : "<<name<<endl;
        }

};
int main()
{
    student s1; 
    // cout<<"rollno is  : "<<s1.rolllno; 
    s1.show(); 
    return 0; 

}