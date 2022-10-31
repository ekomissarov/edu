#include <iostream>
using namespace std;

class Stack
{
    private:
        static const int MAX = 10; // объявление константы допустимо внутри класса
        int st[MAX];
        int top;
    public:
        Stack(): top(0)
        {}
        void push(int var)
        {st[++top] = var;}
        int pop()
        {return st[top--];}
};

int main()
{
    Stack s1;
    s1.push(11);
    s1.push(22);
    s1.push(33);
    cout<<s1.pop()<<endl;
    s1.push(44);
    s1.push(55);
    s1.push(66);
    cout<<s1.pop()<<endl;
    cout<<s1.pop()<<endl;
    cout<<s1.pop()<<endl;
    cout<<s1.pop()<<endl;
    return 0;
}
