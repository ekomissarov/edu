#include <iostream>
using namespace std;

unsigned long fun_rec(unsigned long);
int main ()
{
    cout<<"inf recursion segmentation fault "<<fun_rec(0)<<endl;
    return 0;
}

unsigned long fun_rec(unsigned long n)
{
    return fun_rec(n+1);
}
