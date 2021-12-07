#ifndef PRINTSTRUCT_H
#define PRINTSTRUCT_H

#include <stdio.h>



typedef struct
{
    int ppid;
    int pid;
    char name[30];
    char state;                 // line updated
    char children[10][30];
}process;

typedef union
{
    int count;
    char value;
}temp;

void printStruct(process myProcess, int childcount, temp myUnion);
void printState(int myProcess);
//void printUnion(temp myUnion);

#endif