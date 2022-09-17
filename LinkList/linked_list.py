from typing import Any


class Node:
    def __init__(self, data: Any = None, next_node=None) -> None:
        self.data = data
        self.next = next_node

    def __str__(self) -> str:
        return "Represent the Node in a LinkedList. Next: pointer to next element, Data: Value stored in"


class Linkedlist:
    def __init__(self) -> None:  # define the head of the linked list
        self.head: Node | None = None

    def insert_beginning(self, value: Any) -> None:
        first_node = Node(data=value, next_node=self.head)
        self.head = first_node

    def insert_at_end(self, value: Any) -> None:
        # check linked list is empty, if True, this will be the first element
        if self.head is None:
            first_node = Node(data=value, next_node=self.head)
            self.head = first_node
            return
        """
            Else - linked list is not Empty
            - Create a new node with given value
            - Loop till the last node
            - Point last node's next to new node.
        """
        new_node = Node(data=value, next_node=None)  # last node's next will point on None
        iter_node: Node = self.head
        while iter_node.next:
            iter_node = iter_node.next
        iter_node.next = new_node

    def get_length(self) -> int:
        """ Loop through all the node un till the tail of the linked list """
        count = 0
        iter_node = self.head
        while iter_node:
            iter_node = iter_node.next
            count += 1
        return count

    def insert_at(self, index: int, data: Any) -> None:
        """ check the given index is valid one """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index is Provided")

        if index == 0:
            self.insert_beginning(value=data)
            return
        """
            - loop on linked list
            - increase a counter for rach node when loop
            - if counter == index - 1 # ( to stop at prv index of the target index )
                - make new node with given data and set it's next value as current node's next value
                - set current node's next as new node,
        """
        count = 0
        iter_node: Node = self.head
        while iter_node:
            if count == index - 1:
                new_node = Node(data=data, next_node=iter_node.next)
                iter_node.next = new_node
                break
            count += 1
            iter_node = iter_node.next

    def remove_at(self, index: int) -> None:
        """ check the given index is valid one """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Exception is Provided.")
        #
        """ when remove the head node """
        if index == 0:
            self.head = self.head.next
            return
        #
        count = 0
        iter_node = self.head
        while iter_node:
            if count == index - 1:  # stop at the prv node of the target node.
                iter_node.next = iter_node.next.next
                break
            iter_node = iter_node.next
            count += 1

    def display_linked_list(self):
        """ Print all the Element of an Linked list """
        linked_str: str = ""
        if self.head is None:
            print("Linked list is Empty!")
            return

        itr_node: Node = self.head  # get the first iterator from self.head
        while itr_node:
            linked_str += str(itr_node.data) + " --> "
            itr_node = itr_node.next  # set the next node for itr_node
        print(linked_str)


if __name__ == "__main__":
    link_list = Linkedlist()
    link_list.insert_beginning("Jenny")
    link_list.insert_beginning("Sunny")
    link_list.insert_beginning("Lucy")
    link_list.insert_at_end("JonWik")
    link_list.insert_at(index=0, data="Rosi")
    link_list.insert_at(index=1, data="Ron")
    link_list.remove_at(index=3)
    #
    link_list.display_linked_list()
    print(f"TOTAL LENGTH OF LINKED LIST : {link_list.get_length()}")
