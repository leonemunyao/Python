// The operation of insert an element in the stack is known as pushing 
// and the operation to remove an element from the stack is known as popping. 
// In a stack, we can perform these operations using arrays.

#define LIMIT 100

#include <stdio.h>
#include <stdlib.h>
void push()
{
    int stack[LIMIT], top, element;

    if (top == LIMIT -1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        printf("Enter the element to be inserted:");
        scanf("%d", &element);
        top++;
        stack[top] = element;
    }
}
