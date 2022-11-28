#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if the singly linked list has a cycle in it
 * @list: The singly linked list
 * 
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
listint_t *fast = list;
listint_t *slow = list;

while (fast != NULL && slow != NULL)
{
slow = slow->next;
if (fast->next == NULL)
return (0);
fast = fast->next;
fast = fast->next;

if (fast == slow)
return (1);
}
return (0);
}
