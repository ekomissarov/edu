#include <iostream>
using namespace std;

int main()
{
    void centimze1(double&);
    void centimze2(double*);

    double var = 10.00;
    cout<<var<<" дюймов"<<endl;
    centimze1(var);
    cout<<var<<" сантиметров"<<endl;
    
    var = 10.00;
    cout<<var<<" дюймов"<<endl;
    centimze2(&var);
    cout<<var<<" сантиметров"<<endl;

    return 0;
}

void centimze1(double& v)
{
    v *= 2.54;
}

void centimze2(double* v)
{
    *v *= 2.54;
}
