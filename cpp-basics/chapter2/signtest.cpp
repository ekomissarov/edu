#include <iostream>
using namespace std;
int main()
{
	int signed_var = 1500000000;
    unsigned int unsigned_var = 1500000000;
    signed_var = (signed_var*2)/3; //выход за границы диапазона
    unsigned_var = (unsigned_var*2)/3; //вычисления внутри диапазона
    
    cout<<"Знаковая переменная (после переполнения) = "<<signed_var<<endl;
    cout<<"Беззнаковая переменная = "<<unsigned_var<<endl;
    
    cout<<endl;
    signed_var = 1500000000;
    cout<<"Знаковая переменная = "<<signed_var<<" size: "<<sizeof(signed_var)<<endl;
    signed_var = static_cast<double>(signed_var) * 10 / 10;
    // явное преобразование типа:
    // aCharVar = static_cast<char>(anIntVar)
    cout<<"Знаковая переменная, после преобразования типа = "
        <<signed_var<<" size: "<<sizeof(signed_var)<<endl;
    return 0;
}
