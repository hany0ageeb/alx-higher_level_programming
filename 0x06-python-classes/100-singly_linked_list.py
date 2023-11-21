#!/usr/bin/python3
"""
    This Module defines a Node class and SingleLinkedList class
"""


class Node:
    """
        Node class
        Attributes:
            data(int): node data
            next_node(Node): next node pointer
        Args:
            data(int): data contained in node
            next_node(Node): next node pointer
        Raises:
            TypeError: if data is not integer or next_node is not Node or None
    """
    def __init__(self, data, next_node=None):
        self.data = data

    @property
    def data(self) -> int:
        """
            get/ set Node data attribute
            Args:
                value(int): new value of Node
            Raises:
                TypeError: if value is not int
            Returns:
                (int): Node data value
        """
        return self.__data

    @data.setter
    def data(self, value: int) -> None:
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
            get/set next_node Value
            Args:
                value(Node|None): new value for next_node attrib
            Raises:
                TypeError: if value is not Node or None
            Returns:
                (Node): next_node value or None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value) -> None:
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
        SinglyLinkedList class
        Attributes:
            head(Node): head node of linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
            insert value in sorted manner (ascending)
            Args:
                value(int): new value to insert (should be int)
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            self.__head.next_node = None
        else:
            pre_end_node = None
            end_node = self.__head
            while end_node is not None and value >= end_node.data:
                pre_end_node = end_node
                end_node = end_node.next_node
            if pre_end_node is not None:
                pre_end_node.next_node = new_node
            new_node.next_node = end_node
            if (end_node == self.__head):
                self.__head = new_node

    def __str__(self):
        """
            generate string rep for linkedliist
            Returns:
                (str): string rep for linked list
        """
        value = ""
        visitor = self.__head
        while visitor is not None:
            if visitor.next_node is not None:
                value += f"{visitor.data:d}\n"
            else:
                value += f"{visitor.data:d}"
            visitor = visitor.next_node
        return value
