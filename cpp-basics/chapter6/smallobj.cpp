#include <iostream>
using namespace std;

class smallobj
{
    private:
        int somedata;
    public:
        void setdata(int d)
        {
            somedata = d;
        }
        void showdata()
        {
            cout<<"value somedata = "<<somedata<<endl;
        }
};

int main()
{
    smallobj s1, s2;
    s1.setdata(77);
    s2.setdata(88);
    s1.showdata();
    s2.showdata();
    return 0;
}