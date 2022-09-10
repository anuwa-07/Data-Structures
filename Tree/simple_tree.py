

from dataclasses import dataclass
from typing import Any


class TreeNode:
    def __init__(self, data: Any) -> None:
        self._data = data
        self._children = []
        self._parent = None

    def __str__(self) -> str:
        return f'TreeNode will represent the Tree. Tree is a Recursive DataStructure'
    
    def add_child(self, child):
        child._parent = self
        self._children.append(child)
    
    def get_level(self):
        level = 0
        p = self._parent
        while p:
            level += 1
            p = p._parent
        #
        return level
    
    def print_tree(self):
        spaces = "  " * self.get_level() * 3
        prefix = spaces + "|__" if self._parent else ""
        print(prefix + self._data)
        if len(self._children) > 0: # for leafe nodes we do not have children
            for child in self._children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    # 
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    # 
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    # 
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root



if __name__ == "__main__":
    build_product_tree().print_tree()






