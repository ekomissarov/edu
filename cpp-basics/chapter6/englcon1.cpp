#include <iostream>
using namespace std;

class MulDist
{
    private:
        int mulindex;
    public:
        int pub_val;
        MulDist(): mulindex(2), pub_val(777)
        {}
        MulDist(int m): mulindex(m)
        {}
        void show_mul()
        {
            cout<<"mul_index = "<<mulindex<<endl;
        }
        int get_mul()
        {
            return mulindex;
        }
};

class Distance
{
    private:
        int feet;
        float inches;
    public:
        Distance(): feet(0), inches(0.0) 
        {}
        Distance(int ft, float in): feet(ft), inches(in)
        {}
        void get_dist()
        {
            cout<<"Inp feets: "; cin>>feet;
            cout<<"Inp inches: "; cin>>inches;
        }
        void showdist()
        {
            cout<<feet<<"\' - "<<inches<<"\''"<<endl;
        }
        void add_dist(Distance, Distance);
        void mul_dist(MulDist, Distance);
};

void Distance::add_dist(Distance d2, Distance d3)
{
    inches = d2.inches + d3.inches; // private переменные доступны
    feet=0;
    if (inches >= 12)
    {
        inches-=12;
        feet++;
    }
    feet+=d2.feet + d3.feet;
}

void Distance::mul_dist(MulDist m, Distance d)
{
    feet = (feet + d.feet) * m.get_mul(); // к m.mulindex отсюда нет доступа
    feet = feet*10000 + m.pub_val; // к public полям есть доступ
}

int main()
{
    Distance dist1, dist3;
    Distance dist2(11, 6.25);
    dist1.get_dist();
    dist3.add_dist(dist1, dist2);
    MulDist m;

    cout<<"\ndist1 = "; dist1.showdist();
    cout<<"\ndist2 = "; dist2.showdist();
    cout<<"\ndist3 = "; dist3.showdist();
    cout<<endl;

    dist1.mul_dist(m, dist2);
    cout<<"\ndist1 = "; dist1.showdist();
}
