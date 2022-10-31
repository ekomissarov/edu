#include <iostream>
using namespace std;

int x;
int& setx();

int main()
{
    cout<<"by default global static x = "<<x<<endl;
    setx() = 42;
    cout<<"after setx() = 42, x = "<<x<<endl;
    return 0;
}

int& setx()
{
    // return 3; // ошибка
    // int i = 3;
    // return i; // ошибка т.к. переменная automatic

    return x;
}