#include <iostream>
using namespace std;

int main()
{
    /*
        // Массивы
        T array[maxColumns];
        T value = array[x];
    */

    int data[] = { 1, 2, 3 };
    int i = data[2];
    cout<<i<<endl;

    i = 0;
    void* ptr = data;
    cout<<"(int []) value: -"<<"\taddr: "<<data<<"\tsize: "<<sizeof(data)<<endl;
    cout<<"(int*) value: "<<*static_cast<int*>(ptr)<<"\taddr: "<<ptr<<"\tsize: "<<sizeof(*static_cast<int*>(ptr))<<endl;
    cout<<"---------------------------------------------------------------\n"<<endl;

    ptr = ptr + 2 * sizeof(int);
    i = *static_cast<int*>(ptr);
    //i = *(int*)ptr;
    cout<<"(int*) value: "<<i<<"\taddr: "<<&i<<"\tsize: "<<sizeof(i)<<endl;
    cout<<"---------------------------------------------------------------\n"<<endl;

    int* j = data;
    using array = int*;
    array k = data;
    cout<<k[2]<<endl;

    return 0;
}