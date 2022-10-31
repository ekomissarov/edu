#include <iostream>
using namespace std;
int main()
{
	float rad;
	const float PI = 3.1415926F; // суффикс D - по умолчанию (L - long double)
	/*
	 * float - 3.4*10^-38 .. 3.4*10^38, 7 знаков после запятой (4 байта)
	 * double - 1.7*10^-308 .. 1.7*10^308, 15 знаков после запятой (8 байта)
	 * */
	cout<<"Введите радиус окружности: ";
	cin>>rad;
	
	float area = PI*rad*rad;
	cout<<"Площадь круга = "<<area<<endl;
	cout<<"PI = "<<PI<<endl;
	
    return 0;
}
