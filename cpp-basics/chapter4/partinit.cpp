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
    part part1 = {7777, 88, 199.99F}, part2;

    cout<<"Model: "<<part1.modelnumber<<endl
        <<"prt: "<<part1.partnumber<<endl
        <<"price: "<<part1.cost<<" USD\n"<<endl;

    cout<<"(part) value: -"<<"\taddr: "<<&part1
        <<"\tsize: "<<sizeof(part1)<<endl;
    cout<<"(part1.modelnumber) value:"<<part1.modelnumber
        <<"\taddr: "<<&part1.modelnumber
        <<"\tsize: "<<sizeof(part1.modelnumber)<<endl;
    cout<<"(part1.partnumber) value:"<<part1.partnumber
        <<"\taddr: "<<&part1.partnumber
        <<"\tsize: "<<sizeof(part1.partnumber)<<endl;
    cout<<"(part1.cost) value:"<<part1.cost
        <<"\taddr: "<<&part1.cost
        <<"\tsize: "<<sizeof(part1.cost)<<endl;
    cout<<"-----------------------------------------------------\n"<<endl;

    part2 = part1;

    cout<<"Model: "<<part2.modelnumber<<endl
        <<"prt: "<<part2.partnumber<<endl
        <<"price: "<<part2.cost<<" USD\n"<<endl;

    cout<<"(part) value: -"<<"\taddr: "<<&part2
        <<"\tsize: "<<sizeof(part2)<<endl;
    cout<<"(part2.modelnumber) value:"<<part2.modelnumber
        <<"\taddr: "<<&part2.modelnumber
        <<"\tsize: "<<sizeof(part2.modelnumber)<<endl;
    cout<<"(part2.partnumber) value:"<<part2.partnumber
        <<"\taddr: "<<&part2.partnumber
        <<"\tsize: "<<sizeof(part2.partnumber)<<endl;
    cout<<"(part2.cost) value:"<<part2.cost
        <<"\taddr: "<<&part2.cost
        <<"\tsize: "<<sizeof(part2.cost)<<endl;
    cout<<"-----------------------------------------------------\n"<<endl;


    return 0;
}