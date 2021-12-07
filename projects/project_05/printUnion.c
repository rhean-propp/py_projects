#include "printStruct.h"

void printUnion(temp myUnion) 
{
    printf("Hello World. I'm a Union");
    printf("\tmyUnion: %d %c\n", myUnion.count, myUnion.value);
}