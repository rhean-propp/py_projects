#include "printStruct.h"

void printStruct(process myProcess, int childcount, temp myUnion)
{
    printf("This is the fanciest printing you have ever seen\n");
    printf("==================MYPROCESS==================\n");
    printf("\tNAME: %s\n", myProcess.name);
    printf("\tPID: %d\n", myProcess.pid);
    printf("\tPPID: %d\n", myProcess.ppid);
    //printf("\tSTATE: %c\n", myProcess.state); //state | pass a state from printStruct.py LIne updatded
    //printState(myProcess.state);

    for (int count = 0; count < childcount; count++)
    {
        printf("\t        Child Name: %s\n", myProcess.children[count]);
    }

    printf("==================MYPROCESS==================\n");
    printf("==================MYUNION==================\n");
    printf("\tmyUnion: %d %c\n", myUnion.count, myUnion.value);
    printf("==================MYUNION==================\n");
}