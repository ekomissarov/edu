#include <iostream>
using namespace std;
int main()
{
	int v1 = 100; // объявление, определение (выделение пямяти), присвоение значения
	int v2 = v1 + 1;

	__int8_t v3 = 101;
	__int16_t v4 = 101;
	__int32_t v5 = 101;
	__int64_t v6 = 101;
	
    cout<<"v1 + 10 = "<<v2<<endl;	
	cout<<"int v2 = "<<v2<<"\taddr: "<<&v2<<"\tsizeof: "<<sizeof(v2)<<endl;
	cout<<"__int8_t v3 = "<<v3<<"\taddr: "<<&v3<<"\tsizeof: "<<sizeof(v3)<<endl;
	cout<<"__int16_t v4 = "<<v4<<"\taddr: "<<&v4<<"\tsizeof: "<<sizeof(v4)<<endl;
	cout<<"__int32_t v5 = "<<v5<<"\taddr: "<<&v5<<"\tsizeof: "<<sizeof(v5)<<endl;
	cout<<"__int64_t v6 = "<<v6<<"\taddr: "<<&v6<<"\tsizeof: "<<sizeof(v6)<<endl;
    return 0;
}
