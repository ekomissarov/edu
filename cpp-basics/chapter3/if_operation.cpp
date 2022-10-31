#include <iostream>
using namespace std;
int main ()
{
    int min, alpha = 5, beta = 7;

    if (alpha < beta )
        min = alpha;
    else
        min = beta;

    // is equal to

    min = (alpha < beta) ? alpha : beta;

    cout << min;
    
    cout<<endl;
    return 0;
}