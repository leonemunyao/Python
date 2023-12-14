// The stack elements are displayed in the stack according to the LIFO rule

#define LIMIT 100

#include <stdio.h>
#include <stdlib.h>

void display()
{
    int stack[LIMIT], top, j;
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else if (top > 0)
    {
        printf("The elemens of the stack are:\n");
        for ( j = top; j >= 0; j--)
        {
            printf("%d\n", stack[j]);
        }   
    }
}

int main()
{
    display();
    return (0);
}