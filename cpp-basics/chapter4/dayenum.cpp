#include <iostream>
using namespace std;

int main()
{
    enum days_of_week {Sun = 1, Mon, Tue, Wed, Thu, Fri, Sat};
    days_of_week d1, d2;

    d1 = Mon;
    d2 = Thu;
    int diff = d2 - d1;
    cout<<"days diff: "<<diff<<endl;
    if (d1<d2)
    {
        cout<<"d1 < d2"<<endl;
        cout<<d1<<endl;
        cout<<d2<<endl;
    }
    return 0;
}