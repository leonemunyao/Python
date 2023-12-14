// Stack Overflow - here we are talking about the static memory allocation of data elements of a stack. Therefore if the stack is filled
// completely, then the condition would be called STACK-FULL condition. It is also refered to as stack overflow.

// Stack Underflow - Incase we want to display the data elements of the stack or perform deletion but no elements have been inserted
// in the stack yet, this condition is called STACK-EMPTY. Its also refered to as stack underflow.

#include <stdio.h>
#include <stdlib.h>

#define LIMIT 100

/* Global declaration of variables */

int stack[LIMIT];  // Array implementation of stack
int top;  // To insert and delete data elements
int i;
int choice; // To choose either the three stack operations

void push();
void pop();
void display();

int main()
{
    printf("Welcome to my C Stacks and Queues\n\n");

    printf("Array Iplementation using stacks\n\n");
    top = -1;
    do
    {
        printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n\n");
        printf("Enter your choice:");
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
            display();
            break;
        case 4:
            exit (0);
            break;
        default:
            printf("Sorry, invalid choice!\n");
            break;
        }
    } while (choice != 4);
    return (0);
}

    void push()
    {
        int element;
        if (top == LIMIT -1)
        {
            printf("Stack Overflow\n");
        }
        else
        {
            printf("Enter element to be inserted: ");
            scanf("%d", &element);
            top++;
            stack[top] = element;
        }
    }

    void pop()
    {
        int element;
        if(top == -1)
        {
            printf("Stack Underflow \n");
        }
        else
        {
            element = stack[top];
            printf("The deleted item is %d\n", stack[top]);
            top--;
        }
    }

    void display()
    {
        if (top == -1)
        {
            printf("Stack Underflow\n");
        }
        else if (top > 0)
        {
            printf("The elements of the stack are:\n");
            for (i = top; i >= 0; i--)
            {
                printf("%d\n", stack[i]);
            }
            
        }
        
        
    }