#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @number: number to insert
 * @head: head node
 * Return: he address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node1 = NULL, *node2 = NULL;
	listint_t *new = malloc(sizeof(listint_t));

	if (new != NULL)
	{
		new->n = number;
		if (*head == NULL)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			node1 = *head;
			while (node1 != NULL && node1->n <= number)
			{
				node2 = node1;
				node1 = node1->next;
			}
			new->next = node1;
			if (node2 != NULL)
				node2->next = new;
			else
				*head = new;
		}
	}
	return (new);
}

