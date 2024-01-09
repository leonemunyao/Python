// How to implement a stack in C Programming

// Operations performed on stacks are, push(), pop(), isEmpty() - checks wheter the 
// stack is empty, isFull() - checks whether the stack is full. top() - displays the top most element of the stack.

#include <stdio.h>
#include <stdlib.h>

#define SIZE 4

int top = -1, inp_array[SIZE];
void push();
void pop();
void show();

int main()
{
    int choice;

    while (1)
    {
        printf("Perform operations on the stack:");
        printf("\n1. Push the element\n2. Pop the element\n3. Show\n4. End");
        printf("\n\nEnter the choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            show();
            break;
        case 4:
            exit(0);
    
        default:
            printf("\nInvalid choice!!");
        }
    }
    
}

void push()
{
    int x;

    if (top == SIZE  - 1)
    {
        printf("\nStack Overflow!");
    }
    else
    {
        printf("\nEnter the element to be added in the stack: ");
        scanf("%d", &x);
        top = top + 1;
        inp_array[top] = x;
    }
    
}

void pop()
{
    if (top == -1)
    {
        
    }
    
}