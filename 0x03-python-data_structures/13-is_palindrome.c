#include "lists.h"

/**
 * is_palindrome - a function
 * @head: input
 * Return: 0 if it is not palindrome and else 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_nod = *head, *runner = *head, *reversed = NULL, *next_node;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (runner != NULL && runner->next != NULL)
	{
		runner = runner->next->next;
		next_node = current_nod->next;
		current_nod->next = reversed;
		reversed = current_nod;
		current_nod = next_node;
	}

	if (runner != NULL)
		current_nod = current_nod->next;

	while (reversed != NULL && current_nod != NULL)
	{
		if (reversed->n != current_nod->n)
			return (0);

		reversed = reversed->next;
		current_nod = current_nod->next;
	}

	return (1);
}
