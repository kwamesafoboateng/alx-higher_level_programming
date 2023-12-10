#include "lists.h"

/**
 * check_cycle - function that checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if list has a cycle otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
