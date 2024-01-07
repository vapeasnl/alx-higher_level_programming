#include "lists.h"

/**
 * reverse_listint - reverses
 * @head: pointer
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *currently = *head;
	listint_t *next = NULL;

	while (currently)
	{
		next = currently->next;
		currently->next = previous;
		previous = currently;
		currently = next;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if is a palindrome
 * @head: double pointer
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowly = *head, *faster = *head, *tmp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		faster = faster->next->next;
		if (!faster)
		{
			dup = slowly->next;
			break;
		}
		if (!faster->next)
		{
			dup = slowly->next->next;
			break;
		}
		slowly = slowly->next;
	}

	reverse_listint(&dup);

	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
