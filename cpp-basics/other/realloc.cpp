#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
int main()
{
    const int BUFFER_SIZE = 10;
    char buffer[BUFFER_SIZE];
    char* result = static_cast<char*>(calloc(1, BUFFER_SIZE));
    while(fgets(buffer, 10, stdin))
    {
        strcat(result, buffer);
        if (strchr(buffer, '\n')!=NULL) break;
        result=static_cast<char*>(realloc(result, strlen(result)*2));    
    }

    cout<<"INPUT: "<<result
        <<"STRLEN: "<<strlen(result)<<endl;

    free(result);

    return 0;
}