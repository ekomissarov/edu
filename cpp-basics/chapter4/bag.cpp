#include <iostream>
using namespace std;

struct gem
{
    float mass;
    float price;
};

struct bag
{
    gem a;
    gem b;
};

int main()
{
    bag my_bag = { {1, 30.0F}, {2, 35.5F}};
    cout<<"A) mass: "<<my_bag.a.mass<<"\tprice: "<<my_bag.a.price<<endl
        <<"B) mass: "<<my_bag.b.mass<<"\tprice: "<<my_bag.b.price<<endl;
    return 0;
}

