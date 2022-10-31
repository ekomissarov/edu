#include <iostream>
using namespace std;
// передача переменных по значению (создаются копии на стеке либо копии через регистры)
void repchar(char, int, char='y');

int main()
{
    char ch;
    const int arr[] = {30, 40, 50};
    //arr[0] = 10; //error

    cout<<"Input symbol: "; cin>>ch;
    cout<<"tro-lo-lo"<<endl;
    repchar(ch, arr[0]);
    repchar(ch, arr[1]);
    repchar(ch, arr[2]);

    return 0;
}

void repchar(char ch, int n, char default_ch)
{
    for(int j=0; j<n; j++) cout<<ch;
    cout<<default_ch;
    cout<<endl;
}
