#include <iostream>
using namespace std;

void afunc(int &a, const int& b);

int main()
{
    int alpha = 7, beta = 8;
    afunc(alpha, beta);
    return 0;
}

void afunc(int &a, const int& b)
{
    cout<<"a = "<<a<<" изменяемо"<<endl;
    a=77;
    cout<<"a = "<<a<<" новое значение"<<endl;
    cout<<"b = "<<b<<" константное"<<endl;
    // b = 77; // ошибка

    //передача по ссылке выгодно для передачи больших объектов
}