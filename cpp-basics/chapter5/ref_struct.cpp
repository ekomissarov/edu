#include <iostream>
using namespace std;

struct PointXY
{
    int x;
    int y;
};

void movepoint(PointXY& source_point, PointXY delta_point);

int main()
{
    PointXY current = {1, 1}, dc;
    cout<<"Input dx, dy: "; cin>>dc.x>>dc.y;
    movepoint(current, dc);
    cout<<current.x<<endl
        <<current.y<<endl;

    return 0;
}

void movepoint(PointXY& p, PointXY dp)
{
    p.x += dp.x;
    p.y += dp.y;
}
