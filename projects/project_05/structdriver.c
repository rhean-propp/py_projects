#include "printStruct.h"

int main()
{
    process myproc = {10, 30, "Gary", {"test1", "test2", "test3"}};
    temp t;
    t.count = 0x7A;
    t.count = 0x44;

    printStruct(myproc, 3, t);
    //printUnion(t);

    return 0;
}