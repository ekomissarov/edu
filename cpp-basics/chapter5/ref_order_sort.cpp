#include <iostream>
using namespace std;

int main()
{
    void order(int&, int&);
    void print(int*, int size);

    int values[] = {55, 11, 33, 22, 55, 88, 44};
    const int V_SIZE = sizeof(values)/sizeof(values[0]);

    for (int i=0; i<V_SIZE; i++)
        for (int j=0; j<V_SIZE-1-i; j++)
            order(values[j], values[j+1]);

    print(values, V_SIZE);   
    cout<<endl; 
}

void print(int* arr, int size)
{
    for (int i=0; i<size; i++)
        cout<<*(arr+i)<<" ";
    cout<<endl;
}

void order(int& a, int& b)
{
    if (a>b)
    {
        int tmp;
        tmp = a;
        a = b;
        b = tmp;
    }
}
