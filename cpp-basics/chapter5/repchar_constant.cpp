#include <iostream>
using namespace std;
// передача констант в функцию
void repchar(char, int);

int main()
{
    repchar('-', 43); // для символа используется одинарная кавычка для строки двойная
    cout<<"tro-lo-lo"<<endl;
    repchar('=', 43);
    return 0;
}

void repchar(char ch, int n)
{
    for(int j=0; j<n; j++) cout<<ch;
    cout<<endl;
}
