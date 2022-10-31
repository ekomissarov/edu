#include <iostream>
using namespace std;

class Demo
{
    private:
        int* big_array;
        // const int* big_array; // если так, то метод change не будет работать
        unsigned int l;
    public:
        Demo(): big_array(nullptr), l(0)
        {}
        Demo(int* x, unsigned int l): big_array(x), l(l)
        {}
        void show()
        {
            cout<<"# ";
            for (unsigned int i=0; i<l; i++)
            cout<<big_array[i]<<" ";
            cout<<endl;
        }
        void change(unsigned int i, int val)
        {
            big_array[i] = val;
        }
};

int main()
{
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    Demo d1(arr, 10);
    Demo d2(d1); // работает копирующий конструктор по умолчанию
    d1.show();
    d2.show();

    d1.change(0, 777);

    d1.show();
    d2.show();

    cout<<endl;
}