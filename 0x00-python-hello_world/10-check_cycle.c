#include "lists.h"

/**
 * chk_cyc - function checks if a singly linked list has a cycle
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int chk_cyc(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = slow->next;

	while (slow != NULL && fast->next != NULL
		&& fast->next->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

