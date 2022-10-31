#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {11, 22, 33, 44, 55};

    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++)
    {
        //cout<<arr[i]<<endl;
        cout<<*(arr + i)<<endl; // arr is constant ptr
    }
    cout<<endl;

    int* ptr;
    ptr = arr;

    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++)
    {
        cout<<*ptr++<<endl; // is equal to *(ptr++) because of priority
    }

    return 0;
}