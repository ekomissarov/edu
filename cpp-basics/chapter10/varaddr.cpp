#include <iostream>
using namespace std;

int main()
{
    int var1 = 11;
    int var2 = 22;
    int var3 = 33;
    int* ptr;
    //int *ptr1, *ptr2, *ptr3;

    //int& v; //ошибка - для ссылки требуется инициализатор
    int& v = var3;

    cout<<&var1<<endl;
    cout<<&var2<<endl;
    cout<<&var3<<endl;
    cout<<endl;

    ptr = &var1;
    cout<<"addr:"<<ptr<<" - "<<*ptr<<endl;
    ptr = &var2;
    cout<<"addr:"<<ptr<<" - "<<*ptr<<endl;
    ptr = &var3;
    cout<<"addr:"<<ptr<<" - "<<*ptr<<endl;
    (*ptr)++; // приоритет операции
    cout<<"addr:"<<ptr<<" - "<<*ptr<<endl;
    cout<<endl;

    cout<<v<<" addr:"<<&v<<endl;
    v++;
    cout<<var3<<" addr:"<<&var3<<endl;
    cout<<endl;

    return 0;
}