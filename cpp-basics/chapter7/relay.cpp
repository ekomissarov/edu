#include <iostream>
using namespace std;

int main()
{
    int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int age[4];
    for (int i=0; i<4; i++)
    {
        cout<<"Input age: "; 
        cin>>age[i];
    }
    for (int i=0; i<4; i++)
    {
        cout<<"Your input: "<<age[i]<<endl;
    }
    return 0;
}