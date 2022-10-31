#include <iostream>
using namespace std;

int main()
{
    int int_var;
    float float_var;
    int* ptr_int;
    float* ptr_float;
    void* ptr_void;

    ptr_int = &int_var;
    //ptr_int = float_var; // error
    //ptr_float = int_var; // error
    ptr_float = &float_var;

    ptr_void = &int_var;
    ptr_void = &float_var;

    return 0;
}