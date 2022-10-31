#include <iostream>
using namespace std;
int main()
{
    long dividend, divisor;
    char ch;
    do
    {
        cout<<"Введите делимое: "; cin>>dividend;
        cout<<"Введите делитель: "; cin>>divisor;
        if (divisor==0) break;
        cout<<"Частное равно: "<<dividend/divisor
            <<" Остаток от деления: "<<dividend%divisor<<endl;
        cout<<"Еще? (y/n):"; cin>>ch;
    } while (ch!='n');
    
    return 0;
}