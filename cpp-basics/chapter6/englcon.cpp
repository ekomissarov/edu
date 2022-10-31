#include <iostream>
using namespace std;

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
        void showdist()const
        {
            cout<<feet<<"\' - "<<inches<<"\''"<<endl;
        }
        void add_dist(const Distance&, const Distance&);
};

void Distance::add_dist(const Distance& d2, const Distance& d3)
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

int main()
{
    Distance dist1, dist3;
    Distance dist2(11, 6.25);
    dist1.get_dist();
    dist3.add_dist(dist1, dist2);

    cout<<"\ndist1 = "; dist1.showdist();
    cout<<"\ndist2 = "; dist2.showdist();
    cout<<"\ndist3 = "; dist3.showdist();
    cout<<endl;
    // private переменные dist1.feet и т.п. не доступны
}
