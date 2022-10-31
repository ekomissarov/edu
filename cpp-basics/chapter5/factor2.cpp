#include <iostream>
using namespace std;

unsigned long factfunc(unsigned long);
int main ()
{
    int n=7;
    cout<<n<<"! = "<<factfunc(n)<<endl;
    return 0;
}

unsigned long factfunc(unsigned long n)
{
    // рекурсия
    // переключения контекстов хранятся на стеке
    // каждый экземпляр функции хранит свое n
    if (n>1)
        return n*factfunc(n-1);
    else
        return 1;
}
