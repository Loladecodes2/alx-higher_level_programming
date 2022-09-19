#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: the linked list to be checked
 *
 * Return: 1 if cycle is detected, 0 otherwise
 */

int check_cycle(listint_t *list)
{
    listint_t *slow_p, *fast_p;

    if (!list)
        return (0);
    slow_p = list;
    fast_p = list->next;

    while (fast_p->next && fast_p)
    {
        if (fast_p == slow_p)
            return (1);
        slow_p = slow_p->next;
        fast_p = fast_p->next->next;
    }
    return (0);
}
