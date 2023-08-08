#include "lists.h"

/**
 *insert_node -inserts some number into a singly
 *linked list
 *@head: pointer to head ie first node
 *@number: number to insert
 *Return: address of new node or
 *NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}

/**
 * free_list - Frees a linked list.
 * @head: A pointer to the head of the linked list.
 */
void free_list(listint_t *head)
{
	listint_t *temp;

	while (head)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}

