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
        void showdist()
        {
            cout<<feet<<"\' - "<<inches<<"\''"<<endl;
        }
};

int main()
{
    Distance dist1(11, 6.25);
    Distance dist2(dist1); // работает копирующий конструктор по умолчанию
    Distance dist3 = dist1; // работает копирующий конструктор по умолчанию

    cout<<"\ndist1 = "; dist1.showdist();
    cout<<"\ndist2 = "; dist2.showdist();
    cout<<"\ndist3 = "; dist3.showdist();
    cout<<endl;
}