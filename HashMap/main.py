
from typing import Any


# Make a HashTable or HashMap
class HashTable:
    def __str__(self) -> str:
        return "This is an HashTable, Implement for Testing."

    def __init__(self):
        """
            Here we make the array to store values.
            In this we make an array which length is 10
        """
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key: str) -> int:
        """
            This is the most important part in HashTable.

            Hash tables were design for O(1) time complexity. But it totally depend on the hash_func() you create.
            If you didn't make the function correctly your hash_table can give you O(n) time complexity in search.
            There for You must decide perfect logic for the hash_func by considering the current scenario.
            There is no special way to create hash_func in efficient way, It depend on the scenario.

            Hash_func is use to identify the location you need to save on your HashTable.
            When finding the location it is better to dived final value by len of the HashTable, (10 - in this example).
            -   You need to get the Reminder of that dived value.
            Example:
                value: 14023
                hash_tbl_len = 10
                find the location for store value (14023) : value mod hash_tbl_len
                                                          : 14023 mod 10 => 3 ( reminder )
                So 14023 will store in location 3 in Hash_table.
        :return:int
        """
        _hash: int = 0
        for _char in key:
            _hash += ord(_char)
        #
        return _hash % self.max

    def __getitem__(self, item_index) -> Any:
        """
            This is for the Getting value for the HashTable by KeyName
        :param item_index:
        :return:
        """
        hash_value = self.get_hash(key=item_index)
        return self.arr[hash_value]

    def __setitem__(self, key: str, value: Any) -> None:
        """
            This is for the Storing an Value in a HashTable.
        :param key:
        :param value:
        :return: None
        """
        hash_location: int = self.get_hash(key)
        self.arr[hash_location] = key


if __name__ == "__main__":
    h_table = HashTable()

    value_arr = [
        ["August 1", 129539],
        ["August 12", 694599],
        ["August 3", 984923],
        ["August 4", 483982],
        ["August 25", 593923],
        ["August 6", 435635],
        ["August 7", 213498],
    ]

    for x in value_arr:
        print(f"{x[0]}: ({ h_table.get_hash(x[0])}) -> {x[1]}")
        h_table[x[0]] = x[1]
    print(h_table.arr)

    """
        Results will get like this:
        
        August 1: (4) -> 129539
        August 12: (4) -> 694599
        August 3: (6) -> 984923
        August 4: (7) -> 483982
        August 25: (8) -> 593923
        August 6: (9) -> 435635
        August 7: (0) -> 213498
        #
        ['August 7', None, None, None, 'August 12', None, 'August 3', 'August 4', 'August 25', 'August 6']
        
        Here August 1 is not in HashTable, :( What is happen there is, It was replaced by "August 12", 
        This is Known as "Collism". To avoid this we have few solutions. 
        
            - Open Hashing
                - Chaining
            
            - Closed Hashing
                - Lenear Probing
                - Quadratic Probing
                - Double Probing
    """






