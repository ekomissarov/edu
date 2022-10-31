#include <iostream>
using namespace std;

class Distance
{
    private:
        int feet;
        float inches;
    public:
        Distance(): feet(1), inches(2.2) 
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
    const int MAX = 3;
    Distance dist[MAX] = {{1,2},{2,3},{3,4}}; // C++11 можно так
    
    // можно так:
    // for (int i=0; i<MAX; i++) dist[i]=Distance(i*2, 0);

    // интересно почитать http://www.cyberforum.ru/cpp-beginners/thread1175688.html

    for (int i=0; i<MAX; i++)
    {
        dist[i].showdist();
    }
    cout<<endl;
}
