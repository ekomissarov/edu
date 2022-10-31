#include <iostream>
using namespace std;
int main()
{
	int count = 7;
	float avg_weight = 155.5F;
	double total_weight = count*avg_weight;
	char qq = total_weight*count; // неявное преобразование с переполнением
	
	cout<<"Вес = "<<total_weight<<endl;
	cout<<"QQ = "<<qq<<endl;
	return 0;
}
