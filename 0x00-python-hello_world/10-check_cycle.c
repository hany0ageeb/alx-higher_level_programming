#include "lists.h"
/**
 * check_cycle - check cycle in linked list
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node1 = NULL, *node2 = NULL;

	node1 = node2 = list;
	while (node1 != NULL && node2 != NULL)
	{
		node1 = node1->next;
		if (node2->next != NULL)
			node2 = node2->next->next;
		else
			node2 = NULL;
		if (node1 == node2)
			return (1);
	}
	if (node1 == NULL || node2 == NULL)
		return (0);
	return (1);
}

