#include "lists.h"

/**
 * reverse_listint - reverse linked list
 * @head: head node
 */
void reverse_listint(listint_t **head)
{
	listint_t *nxt = NULL, *pre = NULL;
	listint_t *cur = *head;

	while (cur != NULL)
	{
		nxt = cur->next;
		cur->next = pre;
		pre = cur;
		cur = nxt;
	}
	*head = pre;
}
/**
 * compare_listint - compare lists
 * @h1: first list
 * @h2: second list
 * Return: 1 if equals 0 if not
 */
int compare_listint(listint_t *h1, listint_t *h2)
{
	while (h1 != NULL && h2 != NULL)
	{
		if (h1->n != h2->n)
			return (0);
		h1 = h1->next;
		h2 = h2->next;
	}
	if (h1 == NULL && h2 == NULL)
		return (1);
	return (0);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: linked list head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *pre_slow = NULL, *h1;
	int ret = 0;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		pre_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast == NULL)
	{
		pre_slow->next = NULL;
		reverse_listint(&slow);
		ret = compare_listint(*head, slow);
		reverse_listint(&slow);
		pre_slow->next = slow;
	}
	else
	{
		h1 = slow->next;
		reverse_listint(&h1);
		pre_slow->next = NULL;
		ret = compare_listint(*head, h1);
		reverse_listint(&h1);
		pre_slow->next = slow;
		slow->next = h1;
	}
	return (ret);
}
