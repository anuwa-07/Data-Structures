
"""
    Binary Tree
        - Used for Seraching
        - Can only have max 2 node only.
        - 
"""
from typing import Any

class BinaryTree:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left_node = None
        self.right_node = None
    
    def add_child(self, data: Any) -> None:
        """ Use to add data to the Binary Tree """
        if data == self.data: # not allowed to have duplicate values in B.Tree
            return
        
        if data < self.data: # for adding left side ( small values than base value )
            if self.left_node:
                self.left_node.add_child(data=data)
            else:
                self.left_node = BinaryTree(data=data)
        
        else: # for adding right side ( large values than base value )
            if self.right_node:
                self.right_node = self.right_node.add_child(data=data)
            else:
                self.right_node = BinaryTree(data=data)
        
    def inorder_traversal(self) -> list:
        elements: list = []
        
        if self.left_node:  # Visit to left node
            elements += self.left_node.inorder_traversal()
        
        elements.append(self.data)  # add the base node

        if self.right_node:  # Visit to right node
            elements += self.right_node.inorder_traversal()
        #
        return elements

    def search_in_tree(self, value: Any) -> bool:
        if self.data == value:
            return True
        
        if value < self.data:
            """ Target value is in Left side of Tree """
            if self.left_node:
                return self.left_node.search_in_tree(value=value)
            return False
        
        if value > self.data:
            """ Target value is in Right side of Tree """
            if self.right_node:
                return self.right_node.search_in_tree(value=value)
            return False
    
    def find_max(self) -> Any:
        if self.right_node:
            return self.right_node.find_max()
        return self.data
    
    def find_min(self) -> Any:
        if self.left_node:
            return self.left_node.find_min()
        return self.data

    def delete(self, value: Any) -> Any:
        if value < self.data:
            if self.left_node:
                self.left_node.delete(value=value)
            else:
                return False
        
        if value > self.data:
            if self.right_node:
                self.right_node.delete(value=value)
            else:
                return False
        
        else:
            if self.left_node is None and self.right_node is None:
                return False
            if self.left_node is None:
                return self.right_node
            if self.right_node is None:
                return self.left_node
            # 
            min_value = self.right_node.find_min()
            self.data = min_value
            self.right_node = self.right_node.delete(min_value)
        #
        return self




if __name__ == "__main__":
    root = BinaryTree(data=500)
    root.add_child(1000)
    root.add_child(10)
    print(root.inorder_traversal())
    print(f"Search 100 from the Tree: {root.search_in_tree(value=100)}")
    print(f"Search 500 from the Tree: {root.search_in_tree(value=500)}")
    root.delete(500)
    print(root.inorder_traversal())


