#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head)
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
        slow = slow->next;

    prev->next = NULL;

    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    fast = *head;
    slow = prev;

    while (slow != NULL)
    {
        if (fast->n != slow->n)
            return (0);
        fast = fast->next;
        slow = slow->next;
    }
    return (1);
}