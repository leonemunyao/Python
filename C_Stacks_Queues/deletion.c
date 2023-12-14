// The operation of deletion is known as popping. The deletion of a data element from the stack is done from the top.

#define LIMIT 100
#include <stdio.h>
#include <stdlib.h>

void pop()
{
    int stack[LIMIT], top, element;
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        element = stack[top];
        printf("The deleted item is %d\n", stack[top]);
        top--;
    }
    
}

int main()
{
    pop();
    return (0);
}