#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	long pop1 = 4789426, pop2 = 274124, pop3 = 9761;

	cout << "Город    " << "Нас." << endl
	     << "Москва " << pop1 << endl
	     << "Киров " << pop2 << endl
	     << "Угрюмовка " << pop3 << endl;

	cout << endl;
	cout << setw(15) << "Город" << setw(30) << "Население" << endl
	     << setw(15) << "Москва" << setw(30) << pop1 << endl
	     << setw(15) << "Киров" << setw(30) << pop2 << endl
	     << setw(15) << "Угрюмовка" << setw(30) << pop3 << endl;

    return 0;
}
