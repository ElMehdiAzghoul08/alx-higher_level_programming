#include "lists.h"
/**
 * check_cycle - a function
 * @list: input
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_pointer, *fast_pointer;

	if (list == NULL || list->next == NULL)
		return (0);

	slow_pointer = list;
	fast_pointer = list->next;

	while (fast_pointer != NULL && fast_pointer->next != NULL)
	{
		if (slow_pointer == fast_pointer)
			return (1);
		slow_pointer = slow_pointer->next, fast_pointer = fast_pointer->next->next;
	}

	return (0);
}
