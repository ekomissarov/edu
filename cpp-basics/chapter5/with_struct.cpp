#include <iostream>
using namespace std;

struct PointXY
{
    int x;
    int y;
};

PointXY movepoint(PointXY p, PointXY dp);

int main()
{
    PointXY current = {1, 1}, dc;
    cout<<"Input dx, dy: "; cin>>dc.x>>dc.y;
    current = movepoint(current, dc);
    cout<<current.x<<endl
        <<current.y<<endl;

    return 0;
}

PointXY movepoint(PointXY p, PointXY dp)
{
    p.x += dp.x;
    p.y += dp.y;
    return p;
}
