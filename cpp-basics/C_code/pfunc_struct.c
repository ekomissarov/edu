#include <stdio.h>

int add (int a, int b) { return a+b; }
int sub (int a, int b) { return a-b; }
int mul (int a, int b) { return a*b; }
int div (int a, int b) { return a/b; }

struct _pair {
    int (*fun)(int, int);
    int chr;
};

struct _pair table[] = { {add, '+'}, {sub, '-'}, {mul, '*'}, {div, '/'} };

int main(int argc, char *argv[])
{
    int a,b,op,i;
    
    printf("sizeof(struct _pair) = %ld\n", sizeof(struct _pair));
    
    while(1)
    {
        scanf("%d%lc%d", &a, &op, &b);
        for (i=0; i<sizeof(table)/sizeof(table[0]); i++)
            if (table[i].chr == op)
            {
                printf(" = %d\n", table[i].fun(a,b));
                break;
            }
        if (i>=sizeof(table)/sizeof(table[0])) break;
        
    }
    return 0;
}