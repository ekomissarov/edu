#include <iostream>
using namespace std;
int main()
{
    int a = 2;
    int* ptr = nullptr;
    int*& ptrRef = ptr; // ptrRef ссылается на ptr
    ptrRef = &a; // теперь ptr хранит адрес a
    return 0;
}
