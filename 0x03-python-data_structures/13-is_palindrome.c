#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *last, *end = NULL;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	first = *head;
	while (first != end)
	{
		last = first;
		while (last->next != end)
			last = last->next;
		if (first->n != last->n)
			return (0);
		if (first == last)
			break;
		end = last;
		first = first->next;
	}
	return (1);
}
