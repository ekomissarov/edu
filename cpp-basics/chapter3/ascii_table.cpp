#include <iostream>
using namespace std;

void print_ch(char *i)
{
    cout<<"(char) value: "<<*i<<" addr: "<<static_cast<void*>(i)
        <<" [hex: "<<hex<<static_cast<int>(*i)
        <<", dec: "<<dec<<static_cast<int>(*i)<<"] size: "
        <<sizeof(*i)<<endl;
}

void symb32()
{
    char ch;
    for (int i = 0; i<=32; i++)
    {
        ch = static_cast<char>(i);
        print_ch(&ch);
    }
}

void symb128()
{
    char ch;
    for (int i = 33; i<=127; i++)
    {
        ch = static_cast<char>(i);
        print_ch(&ch);
    }
}

void symb255()
{
    char ch;
    for (int i = 128; i<=255; i++)
    {
        ch = static_cast<char>(i);
        print_ch(&ch);
    }
}

int main ()
{
    symb255();
    return 0;
}