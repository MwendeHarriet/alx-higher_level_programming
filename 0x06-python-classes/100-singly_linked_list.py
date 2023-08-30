#!/usr/bin/python3
"""class Node representing a singly linked list and its attributes"""


class Node:
    """class Node represent a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Initialises a node with parameter data and optional next_node
        Args:
            data (int): the data to be stored in the node
            next_node: the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data to be stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data in the node
        Args:
            value (int): the data to be set
        Raises:
            TypeError: If the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("Data must be an integer.")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list
        Args:
            value (Node): the next node to be set
        Raises:
            TypeError: If the value is not a Node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList representing a singly linked list"""

    def __init__(self):
        """Initialises an empty singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node at value into the linked list
        Args:
            value (int): the value to be inserted into the linked list
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data <= value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Generates a string representation of the linked list
        Returns:
            str: the string representation of the linked list
            """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
