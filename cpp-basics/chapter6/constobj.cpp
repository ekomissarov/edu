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
};


int main()
{
    const Distance dist1(300,0);
    //dist1.get_dist(); // ошибка
    cout<<"\ndist1 = "; dist1.showdist();
    cout<<endl;
}
