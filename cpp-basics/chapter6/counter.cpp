#include <iostream>
using namespace std;

class Counter
{
    private:
        unsigned int count;
    public:
        int publ_int;
        Counter(unsigned int start): count(start), publ_int(start) 
        {
            cout<<"работает конструктор"<<endl;
        } 
        // конструктор, вызывается автоматически при создании каждого из объектов
        // Имя конструктора в точности совпадает с именем класса
        // Нет возвращаемого значения т.к. он автоматически вызывается системой 
        // (не кому возвращать значение)
        // Здесь инициализация расположена между прототипом метода и телом функции
        // для нескольких полей: someClass(): m1(7), m2(8), m3(9) {}
        // Причины, по которым инициализация не проводится в теле конструктора достаточно сложны (??)
        // Такая инициализация someClass(): m1(7), m2(8), m3(9) {}, с помощью списка инициализации
        // происходит до начала исполнения тела конструктора что в некоторых ситуациях бывает важно.
        // список инициализации единственный способ задач анчальные значения констант и ссылок.


        // деструктор, не имеет аргументов и не возвращает значение, 
        // обычно используют для освобождения памяти
        ~Counter() 
        {
            cout<<"деструктор // count = "<<count<<endl;
        }
        void inc_count()
        {count++;}
        int get_count()
        {return count;}
};

void fun(Counter&, const Counter&);

int main()
{
    Counter c1(100), c2(1000);
    cout<<"c1 = "<<c1.get_count()<<endl;
    cout<<"c2 = "<<c2.get_count()<<endl;
    c1.inc_count();
    c1.inc_count();
    c2.inc_count();
    cout<<"c1 = "<<c1.get_count()<<endl;
    cout<<"c2 = "<<c2.get_count()<<endl;
    cout<<"====="<<endl;
    fun(c1, c2);
    cout<<"c1 = "<<c1.get_count()<<endl;
    cout<<"c2 = "<<c2.get_count()<<endl;
    return 0;
}

void fun(Counter& a, const Counter& b)
{
    cout<<"--- function fun begin ---"<<endl;
    cout<<"a = "<<a.get_count()<<endl;
    a.inc_count();
    cout<<"a = "<<a.get_count()<<endl;
    // b.publ_int = 2; // ошибка
    // cout<<b.get_count(); // ошибка
    cout<<"b.publ_int = "<<b.publ_int<<endl;
    b.~Counter(); // нет ошибки, но нахуа это нужно?
    cout<<"--- function fun end ---"<<endl;
}