#include <iostream>
using namespace std;
int main()
{
    int x;
    cout<<"Введите число: "; cin>>x;

    if (x>100)
    {
        cout<<"Это число больше 100"<<endl;
    }
    else
    {
        cout<<"Это число <= 100"<<endl;
    }
    
    
    return 0;
}