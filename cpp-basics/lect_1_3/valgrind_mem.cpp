#include <cstdlib>

int main()
{
    int* data = (int*) malloc(1024);
    return 0;
}

// run: g++ valgrind_mem.cpp -o mem && valgrind ./mem