#include "lists.h"
#include <stdio.h>

/**
 * make_it_doubly_linked - make listint_t a doubly linked list
 * @head: head node
 * Return: pointer to tail node
 */
listint_t *make_it_doubly_linked(listint_t *head)
{
	listint_t *v = NULL;

	if (head != NULL && head->next != NULL)
	{
		head->previous = NULL;
		v = head;
		while (v->next != NULL)
		{
			v->next->previous = v;
			v = v->next;
		}
	}
	return (v);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *last;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	last = make_it_doubly_linked(*head);
	first = *head;
	while (first->previous != last && first != last)
	{
		if (first->n != last->n)
			return (0);
		first = first->next;
		last = last->previous;
	}
	return (1);
}
