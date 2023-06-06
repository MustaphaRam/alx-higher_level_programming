#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number
 * @head: pointer to pointer of first node of listint_t list
 * @number: number integer
 *
 * Description: inserts a number into a sorted singly linked list
 *
 * Return: the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));

    if (new_node == NULL)
        return NULL;

    new_node->n = number;

    if (*head == NULL || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        listint_t *current = *head;

        while (current->next != NULL && number > current->next->n)
            current = current->next;
        new_node->next = current->next;
        current->next = new_node;
    }
    return new_node;
}