#include "lists.h"

/**
 * _is_palindrome - recursively check if listint_t is palindrome
 * @first: first node
 * @last: last_node
 * Return: 0 if it is not a palindrome, 1 if it is
 */
static int _is_palindrome(listint_t *first, listint_t **last)
{
	int ret_code = 0;

	if (first == NULL)
		return (1);
	if (_is_palindrome(first->next, last) != 1)
		return (0);
	if (first->n == (*last)->n)
		ret_code = 1;
	*last = (*last)->next;
	return (ret_code);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	return (_is_palindrome(*head, head));
}
