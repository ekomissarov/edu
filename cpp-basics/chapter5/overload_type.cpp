#include <iostream>
using namespace std;
// передача переменных по значению (создаются копии на стеке либо копии через регистры)
void print(int);
void print(bool);
void print(const char*);
void print(const string&);

int main()
{
    print(77);
    print(true);
    print("qwertyqqqq");
    
    string tt;
    tt = "qwerty asdfgh";
    cout<<tt<<endl;
    print(tt);
    

    return 0;
}

void print(int x) // 1
{
    cout<<x<<endl;
}

void print(bool x) // 2
{
    cout<<(x ? "true" : "false")<<endl;
}

void print(const char* x) // 3
{
    cout<<"const char* "<<*x<<endl;
}

void print(const string& x) // 4
{
    cout<<"string: "<<x<<endl;
}
