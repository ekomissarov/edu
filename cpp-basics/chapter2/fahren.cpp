#include <iostream>
using namespace std;
int main()
{
	int ftemp;
	cout<<"Введите температуру по фаренгейту: ";
	cin>>ftemp;
	
	int ctemp = (ftemp-32)*5/9;
	cout<<"Температура по цельсию = "<<ctemp<<endl;
    return 0;
}
