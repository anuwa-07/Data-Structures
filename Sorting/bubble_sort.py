

def bubble_sort(data_set: list) -> list:
    number_of_elements: int = len(data_set)

    for i in range(number_of_elements):
        flag: int = 0
        for j in range(0, number_of_elements-1-i):
            if data_set[j] > data_set[j+1]:
                flag = 1
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]
        if flag == 0:
            break  # If there is Zero swapping, we do not need to continue sorting, It already sorted!
    return data_set


if __name__ == "__main__":
    scores = [12, 34, 54, 6, 7, 122, 54, 86, 64]
    sorted_score: list = bubble_sort(data_set=scores)
    #
    print(f"Before the sort: {scores}")
    print(f"After the sort: {sorted_score}")


'''
---------------------------------------------------------------------------------------
# Bubble sort
---------------------------------------------------------------------------------------
- (n) total elements
- Total Number of comparison need: n(n+1)/2 => O(n^2)
- Total Number of Swaps: n(n-1)/2 => O(n^2)


Bubble Sort can covert as Adaptive, By default it is not Adaptive,
    Adaptive: 
        - If list sort take less time when we try to sort already sorted list, That sorting algorithm is Adaptive.

'''

