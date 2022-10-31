#include <iostream>
using namespace std;
// передача переменных по значению (создаются копии на стеке либо копии через регистры)
void repchar();
void repchar(char);
void repchar(char, int, char='y'); // параметры по умолчанию указываются в прототипе

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

    repchar(ch);
    repchar();


    return 0;
}

void repchar(char ch, int n, char default_ch)
{
    for(int j=0; j<n; j++) cout<<ch;
    cout<<default_ch;
    cout<<endl;
}

void repchar(char ch)
{
    for(int j=0; j<10; j++) cout<<ch;
    cout<<endl;
}

void repchar()
{
    for(int j=0; j<10; j++) cout<<'#';
    cout<<endl;
}


