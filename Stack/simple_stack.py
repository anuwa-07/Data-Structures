
from dataclasses import dataclass
from typing import Any


# Implemanet a simple Array
@dataclass
class Stack:
    size: int
    top: int
    stack_: list



class SimpleStack:

    def __init__(self, stack: Stack):
        self.__stack: Stack = Stack(size=10, top=-1, stack_=[])
    
    def get_stacktop(self) -> Any:
        if(self.__stack.top == -1):
            return None
        return self.__stack.stack_[self.__stack.top]
    
    def is_empty(self) -> bool:
        if (self.__stack.top == 0):
            return True
        return False
    
    def is_full(self) -> bool:
        if (self.__stack.top == self.__stack.size - 1):
            return True
        return False

    def push(self, value: Any) -> None:
        '''
            - Increase the Top
            - Add value to the End
            - Insert value. But before Insert we have to make sure "Stack" is not Empty
        '''
        if (self.__stack.top == self.__stack.size - 1):
            raise Exception("Stack is Full! Unable to Insert Elements!")
        self.__stack.top = self.__stack.top + 1
        self.__stack.stack_[self.__stack.top] = value
    
    def pop(self) -> Any:
        '''
            - Make sure top is not empty
            - Remove top Element
            - top = top - 1
        '''
        pop_value:Any = -1
        if (self.__stack.top == -1 ):
            raise Exception("Stack is already empty")
        
        pop_value = self.__stack.stack_[self.__stack.top]
        self.__stack.top = self.__stack.top - 1
        #
        return pop_value
    
    def find_at(self, positon) -> Any:
        '''
            To find a value in a Given Index
            Formiula: 
                position: int
                index:int = top - position + 1
        '''
        find_value: Any = -1
        if (self.__stack.top - positon + 1 < 0 ):
            raise Exception("Invald Position!")
        find_value = self.__stack.stack_[self.__stack.top - positon + 1]
        #
        return find_value







