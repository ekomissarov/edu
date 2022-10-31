#include <iostream>
#include <cstdint>
using namespace std;

void print_ch(char *i)
{
    cout<<"(char) value: "<<*i<<" addr: "<<static_cast<void*>(i)
        <<" [hex: "<<hex<<static_cast<int>(*i)
        <<", dec: "<<dec<<static_cast<int>(*i)<<"] size: "
        <<sizeof(*i)<<endl;
}

void example1()
{
    // Если указатель никуда не ссылается,
    // надо использовать nullptr
    void* invalid = nullptr;
    int val=0x77889969;
    void* addr = &val;
    cout<<"BASE int value: "<<val<<"\thex: "<<hex<<val<<dec<<"\taddr: "<<addr<<"\tsize: "<<sizeof(val)<<endl;
    cout<<"----------------------------------------------------------------------------------------"<<endl;

    size_t size = sizeof(addr); // размер адреса
    cout<<"(void) value: n/a"<<"\taddr: "<<addr<<"\tsize: "<<size<<endl; // *addr - нельзя

    int* int_val = static_cast<int*>(addr);
    size = sizeof(*int_val);
    cout<<"(int) value: "<<*int_val<<"\taddr: "<<int_val<<"\tsize: "<<size<<endl;

    char* ch = static_cast<char*>(addr);
    print_ch(ch);

    unsigned short* srt_val = static_cast<unsigned short*>(addr);
    size = sizeof(*srt_val);
    cout<<"(short) value: "<<*srt_val<<"\taddr: "<<srt_val
    <<" [hex: "<<hex<<static_cast<int>(*srt_val)<<"]\tsize: "<<dec<<size<<endl;
    cout<<"----------------------------------------------------------------------------------------"<<endl;
}

void example2()
{
    int val=0x77886699;
    void* addr = &val;
    cout<<"BASE int value: "<<val<<"\thex: "<<hex<<val<<dec<<"\taddr: "<<addr<<"\tsize: "<<sizeof(val)<<endl;
    cout<<"----------------------------------------------------------------------------------------\n"<<endl;

    int16_t* i16 = static_cast<int16_t*>(addr);
    for (int i=0; i<sizeof(val)/sizeof(*i16); i++)
    {
        cout<<"(int16_t) value: "<<*i16<<"\taddr: "<<i16
        <<" [hex: "<<hex<<static_cast<int>(*i16)<<"]\tsize: "<<dec<<sizeof(*i16)<<endl;
        i16++;
    }
    cout<<"----------------------------------------------------------------------------------------\n"<<endl;
}

void example3()
{
    int val=0x61626364;
    void* addr = &val;
    cout<<"BASE int value: "<<val<<"\thex: "<<hex<<val<<dec<<"\taddr: "<<addr<<"\tsize: "<<sizeof(val)<<endl;
    cout<<"----------------------------------------------------------------------------------------"<<endl;
    cout<<"little endian:\n"<<endl;

    char* charPtr = static_cast<char*>(addr);
    for (int i=0; i<sizeof(val);i++) print_ch(charPtr++);
    cout<<endl;
}

int main()
{
    example2();
    return 0;
}