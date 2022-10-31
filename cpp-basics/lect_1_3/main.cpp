#include "square.h"

int main()
{
    return square(2);
}

// g++ -c main.cpp 
// objdump -d -r main.o
// g++ -o my_prog main.o square.o
// echo $?