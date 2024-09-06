#!/usr/bin/python3
"""
Module for Linked-list in a Pythonic way.
"""


class Node:
    """
    Class Node:
        - Defines a node of a singly linked list.
        - Has private attributes `data` and `next_node`.
    """
    def __init__(self, data, next_node=None):
        """
        Instantiation:
            - Private instance attribute: data
            - Private instance attribute: next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Data property:
            - Property to retrieve the data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Data Setter:
            - Sets the data attribute.
            - Ensures the data is an integer.
            - Raises TypeError if it's not.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Next Node property:
            - Property to retrieve the next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Next Node Setter:
            - Sets the next_node attribute.
            - Ensures next_node is either None or a Node object.
            - Raises TypeError if it's not.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class SinglyLinkedList:
        - Defines a singly linked list.
        - Has a private instance attribute `head`.
    """
    def __init__(self):
        """
        Instantiation:
            - Initializes the list with `head` as None.
        """
        self.__head = None

    def __str__(self):
        """
        String representation:
            - Prints the entire list, one node per line.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Public method:
            - Inserts a new Node into the list at the correct sorted position.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse to find the correct spot.
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
