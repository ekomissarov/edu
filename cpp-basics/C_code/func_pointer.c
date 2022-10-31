#include <stdio.h>

int add (int a, int b) { return a+b; }
int sub (int a, int b) { return a-b; }
int mul (int a, int b) { return a*b; }
int div (int a, int b) { return a/b; }

int (*table[])(int, int) = { add, sub, mul, div };

int main(int argc, char *argv[])
{
    int a,b,c;
    
    printf("sizeof(table) = %ld\n", sizeof(table));
    printf("sizeof(table[0]) = %ld\n", sizeof(table[0]));
    
    scanf("%d%d%d", &a, &b, &c);
    while(c < sizeof(table)/sizeof(table[0]))
    {
        printf(" = %d\n", table[c](a,b));
        scanf("%d%d%d", &a, &b, &c);
    }
    return 0;
}