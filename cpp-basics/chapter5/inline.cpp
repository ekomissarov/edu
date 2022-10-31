#include <iostream>
using namespace std;

inline float lbstokg(float);
// inline это рекомендяция
// в случае например, если существует указатель на функцию,
// компилятор не сможет сделать ее встраиваемой

int main ()
{
    cout<<"5lbs = "<<lbstokg(5)<<"kg"<<endl;
    return 0;
}

inline float lbstokg(float pounds)
{
    return 0.453592 * pounds;
}
