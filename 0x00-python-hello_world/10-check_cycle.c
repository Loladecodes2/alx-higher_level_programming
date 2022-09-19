#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: the linked list to be checked
 *
 * Return: 1 if cycle is detected, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL)
		return (0);

	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
