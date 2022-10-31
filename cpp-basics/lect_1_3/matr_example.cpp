#include <iostream>
using namespace std;

int main()
{
    /*
        // Двумерные массивы
        T array[maxRows][maxColumns];
        T value = array[y][x];
    */
    const int maxColumns = 2;
    int matrix[][2] = { { 1, 2 },  { 3, 4 }, { 5, 6 } };
    int i = matrix[2][1];
    cout<<i<<endl;

    void* ptr = matrix;
    void* begin = matrix;
    cout<<"(int [][]) value: -"<<"\taddr: "<<matrix<<"\tsize: "<<sizeof(matrix)<<endl;
    cout<<"(int*) value: "<<*static_cast<int*>(ptr)<<"\taddr: "<<ptr<<"\tsize: "<<sizeof(*static_cast<int*>(ptr))<<endl;
    cout<<"---------------------------------------------------------------\n"<<endl;


    ptr = ptr + maxColumns * sizeof(int) * 2 + sizeof(int);
    i = *static_cast<int*>(ptr);
    //i = *(int*)ptr;
    cout<<"(int*) value: "<<i<<"\taddr: "<<&i<<"\tsize: "<<sizeof(i)<<endl;
    cout<<"---------------------------------------------------------------\n"<<endl;

    ptrdiff_t d1 = static_cast<int*>(ptr) - static_cast<int*>(begin);
    char* c1 = static_cast<char*>(begin);
    char* c2 = static_cast<char*>(ptr);
    ptrdiff_t d2 = c2 - c1; // d2 == 8

    cout<<"diff (in int items): "<<d1<<endl
        <<"diff (in char items): "<<d2<<endl;
    cout<<"---------------------------------------------------------------\n"<<endl;

    void* j = matrix;
    using matr = int(*)[2];
    matr k = static_cast<matr>(j);
    cout<<k[2][1]<<endl;

    return 0;
}