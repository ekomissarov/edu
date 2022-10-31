#include <iostream>
using namespace std;

const int X = 2;
const int Y = 2;
const int Z = 2;

void display(int [][Y][Z]); // X указывать не обязательно

int main()
{
    int arr[X][Y][Z]=
    {
        {
            {111, 112}, 
            {121, 122}
        },
        {
            {211, 212},
            {221, 222}
        },
    };
    display(arr);
    cout<<endl;
    cout<<arr[0][0][0]<<endl; // передача по ссылке
}

void display(int s[][Y][Z]) // X указывать не обязательно
{
    int x,y,z;
    s[0][0][0]=7777;
    for (x=0; x<X; x++) for (y=0; y<Y; y++)for (z=0; z<Z; z++)
    {
        cout<<"X: ["<<x<<"] Y ["<<y<<"] Z ["<<z<<"]: ";
        cout<<s[x][y][z]<<endl;
    }

}