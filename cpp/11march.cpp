/*
hirearchical inheritance : multiple  derivred class inherit same base class .

class a 
class b : public a 
class c : public a 
*/

#include <iostream>
using namespace std;
class animal 
{
    private : 
        string name; 
    public : 
        animal(string n)
        {
            name =n; 
        }
}; 
class dog : public animal
{
    public : 
        string breed;
        dog(string n,string b) :animal(n)
        {
            breed = b;
        }
    void sound()
    {
        cout<<"bark"<<"\n";
    }
};
class cat : public animal 
{
    public : 
        int age; 
    cat(string n,int a):animal(n)
    {
        age =a; 
    }
    void sound()
    {
        cout<<"meow"<<"\n";
    }
};

int main()
{
    cat c("kitty",5); 
    c.sound(); 
    dog d("rover","corgi");
    d.sound();
    return 0; 
}