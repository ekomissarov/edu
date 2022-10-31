#include <iostream>
using namespace std;
int main ()
{
    int speed;
    cout<<"Input speed 33,45,78: "; cin>>speed;
    switch (speed)
    {
        case 33:
            cout<<"long play format"<<endl;
            break;
        case 45:
            cout<<"Single format"<<endl;
            break;
        case 78:
            cout<<"Deprecated format"<<endl;
            //break;
        default:
            cout<<"Unknown format"<<endl;
            break;
    }
    cout<<endl;
    return 0;
}