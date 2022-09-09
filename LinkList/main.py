
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def inster_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        #
        itr.next = Node(data, None)
    
    def insert_value(self, data_list):
        for data in data_list:
            self.inster_at_end(data)

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
        count += 1


    def remove_at(self, index:int):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid Index!")
        
        if index == 0:
            '''When trying to remove the head element'''
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1



    def print(self):
        if self.head is None:
            print("Linked list is Empty")
            return
        
        itr = self.head
        link_str = ''
        while itr:
            link_str += str(itr.data) + "--->"
            itr = itr.next
        print(link_str)




if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining("Sauron")
    ll.insert_at_begining("Sam")
    ll.inster_at_end(["Jhone", "Argon", "Gimly", "Gandolf"])
    ll.remove_at(1)
    ll.insert_at(1, "Bilbo")
    
    ll.print()





