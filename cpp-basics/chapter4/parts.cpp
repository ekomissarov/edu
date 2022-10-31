#include <iostream>
using namespace std;

struct part
{
    int modelnumber;
    int partnumber;
    float cost;
};


int main ()
{
    part my_test_part;
    my_test_part.modelnumber = 7777;
    my_test_part.partnumber = 88;
    my_test_part.cost = 199.99F;

    cout<<"Model: "<<my_test_part.modelnumber<<endl
        <<"prt: "<<my_test_part.partnumber<<endl
        <<"price: "<<my_test_part.cost<<" USD\n"<<endl;

    cout<<"(part) value: -"<<"\taddr: "<<&my_test_part
        <<"\tsize: "<<sizeof(my_test_part)<<endl;
    cout<<"(my_test_part.modelnumber) value:"<<my_test_part.modelnumber
        <<"\taddr: "<<&my_test_part.modelnumber
        <<"\tsize: "<<sizeof(my_test_part.modelnumber)<<endl;
    cout<<"(my_test_part.partnumber) value:"<<my_test_part.partnumber
        <<"\taddr: "<<&my_test_part.partnumber
        <<"\tsize: "<<sizeof(my_test_part.partnumber)<<endl;
    cout<<"(my_test_part.cost) value:"<<my_test_part.cost
        <<"\taddr: "<<&my_test_part.cost
        <<"\tsize: "<<sizeof(my_test_part.cost)<<endl;
    cout<<"-----------------------------------------------------\n"<<endl;

    return 0;
}