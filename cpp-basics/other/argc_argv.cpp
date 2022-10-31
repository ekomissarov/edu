#include <iostream> 
#include <cstdlib> 
using namespace std;

int main(int argc, char* argv[]) 
{ 

    cout<<argc<<endl;
    int x = atoi(argv[1]);
    cout << "x=" << x << endl;
    int y =  atoi(argv[2]);
    cout << "y=" << y << endl;

    return 0; 
}