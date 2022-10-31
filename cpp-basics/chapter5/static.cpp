#include <iostream>
using namespace std;

float getavg(float);

int main()
{
float getavg(float);
    float data=1, avg;
    while (true)
    {
        cout<<"Input float number: "; cin>>data;
        if (data == 0) break;
        avg = getavg(data);
        cout<<"Average = "<<avg<<endl;
    }
    return 0;
}

float getavg(float newdata)
{
    static float total; // by default static local is 0
    static int count;
    count++;
    total += newdata;
    return total/count;
}
