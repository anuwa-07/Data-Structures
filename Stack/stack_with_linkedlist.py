
from dataclasses import dataclass
from typing import Any

# Fist we need to have a Node
@dataclass
class Node:
    data: Any
    next: Any

@dataclass
class Stack:
    top: int
    linkedlist: list


class LinkedStack:
    def __init__(self) -> None:
        self.__node = Node(data=None, next=None)
    
    def is_empty():
        ...

    











